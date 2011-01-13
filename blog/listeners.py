from django.contrib.comments.signals import comment_was_posted
from django.contrib.comments.models import Comment
from django.core.mail import send_mail
from django.template import loader, Context
from django.core.mail import EmailMultiAlternatives
from lawrencetrailhawks.members.models import Member



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

from django.contrib.comments.signals import comment_was_posted

def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target
    # Model
    #if comment.content_type.model_class() != Entry:
    #    return

    from django.contrib.sites.models import Site
    from django.conf import settings

    try:
        from lawrencetrailhawks.lth.akismet import Akismet
    except:
        return

    # use TypePad's
    # AntiSpam if
    # the key is
    # specified in
    # settings.py
    if hasattr(settings, 'TYPEPAD_ANTISPAM_API_KEY'):
        ak = Akismet(key=settings.TYPEPAD_ANTISPAM_API_KEY,
                  blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain)
        ak.baseurl = 'api.antispam.typepad.com/1.1/'
    else:
        ak = Akismet(key=settings.AKISMET_API_KEY,
                     blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain )

    if ak.verify_key():
         data = {
             'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
             'user_agent': request.META.get('HTTP_USER_AGENT', ''),
             'referrer': request.META.get('HTTP_REFERER', ''),
             'comment_type': 'comment',
             'comment_author': comment.user_name.encode('utf-8'),
             }

    if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
        comment.flags.create(
            user=comment.content_object.author,
            flag='spam')
        comment.is_public = False
        comment.save()


comment_was_posted.connect(on_comment_was_posted)
comment_was_posted.connect(notify_admins)
comment_was_posted.connect(notify_commenters)
