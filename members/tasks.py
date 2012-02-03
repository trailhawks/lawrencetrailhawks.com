from __future__ import absolute_import

import datetime

from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.core.mail import send_mail

from .models import Member


# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(minute='*', day_of_week="*"))
def monthly_notice():
    today = datetime.datetime.today()
    exp_date = datetime.date(today.year, today.month + 1, today.day)
    members = Member.objects.filter(active=True, date_paid=datetime.date(exp_date.year - 1, exp_date.month, exp_date.day))
    if members.count > 0:
        for member in members:
            body = """
Hello %s,

It's me, the Magical Trailhawk Genie here, I just wanted to let you know that your membership is about to expire on %s.

If you'd like to renew your membership please you can pay online through UltraSignup.com at http://ultrasignup.com/register.aspx?did=7418.

If you have any questions please email Gary at unews@ultrastory.com.

Thanks

Magical Trailhawk Genie
""" % (member.full_hawk_name, member.date_expires)

            subject = "Your trailhawk membership is about to expire"
            send_mail(subject, body, 'do-not-replay@lawrencetrailhawks.com', [member.email], fail_silently=False)
