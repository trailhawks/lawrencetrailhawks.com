from django.contrib.comments.signals import comment_was_posted
from django.contrib.comments.models import Comment
from django.template import loader, Context
from django.core.mail import EmailMultiAlternatives
from lawrencetrailhawks.members.models import Member

from django.utils.encoding import smart_str
from lawrencetrailhawks.lth import akismet
from django.conf import settings
from django.contrib.sites.models import Site

AKISMET_API_KEY = getattr(settings, "AKISMENT_API_KEY", "f9c9f57988a4")

def moderate_comment(sender, comment, request, **kwargs):
    ak = akismet.Akismet(
        key = AKISMET_API_KEY,
            blog_url = 'http://%s/' % Site.objects.get_current().domain
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
        notify_commenters(sender, **kwargs)
        notify_admins(sender, **kwargs)

comment_was_posted.connect(moderate_comment)




def notify_commenters(sender, **kwargs):
    comment = kwargs.get('comment')
    subject = "[lawrencetrailhawks.com]: %s commented on %s" % (comment.user_name, comment.content_object.title)
    c = Context({'comment': comment})
    t = loader.get_template("email_body.txt")
    txt_body = "%s said:\n\n %s" % (comment.user_name, comment.comment)
    notify_list = list(set([x.email for x in Comment.objects.filter(object_pk=comment.content_object.pk)]))
    notify_list.remove(comment.user_email)

    email = EmailMultiAlternatives(subject,
            txt_body,
            from_email='no-reply@lawrencetrailhawks.com',
            to=['admin@lawrencetrailhawks.com'],
            bcc=notify_list)
    email.attach_alternative(t.render(c), "text/html")
    email.send()


def notify_admins(sender, **kwargs):
    comment = kwargs.get('comment')
    subject = "[lth-admin]: %s commented on %s" % (comment.user_name, comment.content_object.title)
    c = Context({"comment":comment})
    t = loader.get_template("admin_body.txt")
    txt_body = "%s said:\n\n %s" % (comment.user_name, comment.comment)

    officers = [officer.email for officer in Member.objects.filter(position__isnull=False)]
    email = EmailMultiAlternatives(subject,
            txt_body,
            from_email="no-reply@lawrencetrailhawks.com",
            to=officers)
    email.attach_alternative(t.render(c), "text/html")
    email.send()



