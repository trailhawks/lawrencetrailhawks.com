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
    subject = "[lth-admin]: %s commented on %s" % (comment.user_name, comment.content_type.title)
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

comment_was_posted.connect(notify_admins)
comment_was_posted.connect(notify_commenters)
