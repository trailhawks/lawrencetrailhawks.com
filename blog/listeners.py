from django.conf import settings
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_posted
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from django.utils.encoding import smart_str

from lth import akismet
from members.models import Member


AKISMET_API_KEY = getattr(settings, 'AKISMET_API_KEY', '')


def moderate_comment(sender, comment, request, **kwargs):
    ak = akismet.Akismet(
        key=AKISMET_API_KEY,
        blog_url='http://%s/' % Site.objects.get_current().domain
    )
    data = {
        'user_ip': request.META.get('REMOTE_ADDR', ''),
        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
        'referrer': request.META.get('HTTP_REFERRER', ''),
        'comment_type': 'comment',
        'comment_author': smart_str(comment.user_name),
    }
    if ak.comment_check(smart_str(comment.comment), data=data, build_data=True):
        comment.is_public = False
        comment.save()

    if comment.is_public:
        notify_commenters(sender, comment, **kwargs)
        notify_admins(sender, comment, **kwargs)

comment_was_posted.connect(moderate_comment)


def notify_commenters(sender, comment, **kwargs):
    subject = "[lawrencetrailhawks.com]: %s commented on %s" % (comment.user_name, comment.content_object)
    c = Context({'comment': comment})
    t = loader.get_template("email_body.txt")
    txt_body = "%s said:\n\n %s" % (comment.user_name, comment.comment)

    notify_list = list(set(Comment.objects.filter(object_pk=comment.content_object.pk).values_list('user_email', flat=True)))

    try:
        notify_list.remove(comment.user_email)
    except:
        pass

    if len(notify_list):
        email = EmailMultiAlternatives(subject,
            txt_body,
            from_email='no-reply@lawrencetrailhawks.com',
            to=['admin@lawrencetrailhawks.com'],
            bcc=notify_list)
        email.attach_alternative(t.render(c), "text/html")
        email.send()


def notify_admins(sender, comment, **kwargs):
    subject = "[lth-admin]: %s commented on %s" % (comment.user_name, comment.content_object)
    c = Context({"comment": comment})
    t = loader.get_template("admin_body.txt")
    txt_body = "%s said:\n\n %s" % (comment.user_name, comment.comment)
    notify_list = set(Member.comment_email_objects.values_list('email', flat=True))

    try:
        maintainer = comment.content_object.contact.email
        notify_list.add(maintainer)
    except:
        # Add race leaders and run leaders to notification list
        pass

    notify_list = list(notify_list)

    email = EmailMultiAlternatives(subject,
            txt_body,
            from_email="no-reply@lawrencetrailhawks.com",
            to=notify_list,
            bcc=['admin@lawrencetrailhawks.com'])
    email.attach_alternative(t.render(c), "text/html")
    email.send()
