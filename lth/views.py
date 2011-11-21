import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from lawrencetrailhawks.members.models import Member


@login_required
def member_list(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_list.csv'

    members = Member.objects.active()
    member_list = csv.writer(response)
    member_list.writerow(["First Name",
                         "Last Name",
                         "Hawk Name",
                         "Gender",
                         "Club Officer Title",
                         "Address",
                         "Address2",
                         "City",
                         "State",
                         "Zip",
                         "Email Address",
                         "Date paid",
                         "Member Since",
                         "Dues Due"])

    for member in members:
        member_list.writerow([member.first_name,
                             member.last_name,
                             member.hawk_name,
                             dict(Member.GENDER_CHOICES).get(member.gender, None),
                             dict(Member.POSITION_CHOICES).get(member.position, None),
                             member.address,
                             member.address2,
                             member.city,
                             member.state,
                             member.zip,
                             member.email,
                             member.date_paid,
                             member.member_since,
                             member.date_expires])

    return response
