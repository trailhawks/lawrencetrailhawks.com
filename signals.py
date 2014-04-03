import json

from django.core.mail import EmailMessage
from django.dispatch import receiver
from djrill.signals import webhook_event


@receiver(webhook_event)
def handle_bounce(sender, event_type, data, **kwargs):
    if event_type == 'hard_bounce' or event_type == 'soft_bounce':
        print "Message to %s bounced: %s" % (
            data['msg']['email'],
            data['msg']['bounce_description']
        )


@receiver(webhook_event)
def handle_inbound(sender, event_type, data, **kwargs):
    if event_type == 'inbound':
        print "Inbound message from %s: %s" % (
            data['msg']['from_email'],
            data['msg']['subject']
        )
    json_body = json.dumps(data, indent=2)
    msg = EmailMessage(subject=event_type, from_email='board@lth.im', to=['jeff.triplett@gmail.com'], body=json_body)
    msg.send()
