from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from lawrencetrailhawks.members.models import Member
import csv
import StringIO

PRESIDENT = 1
VICE_PRESIDENT = 2
TREASURER = 3
SECRETARY = 4
WEB_MASTER = 5
POSITION_CHOICES = (
    (PRESIDENT, "President"),
    (VICE_PRESIDENT, "Vice President"),
    (TREASURER, "Treasurer"),
    (SECRETARY, "Secretary"),
    (WEB_MASTER, "Web Master"),
)



@login_required
def member_list(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_list.csv'

    members = Member.objects.filter(active=True)
    member_list = csv.writer(response)
    member_list.writerow(["First Name", "Last Name", "Club Officer Title", "Address", "Email Address","Date paid", "Member Since",  "Dues Due"])

    for member in members:
        member_list.writerow([member.first_name,
                             member.last_name,
                             dict(POSITION_CHOICES).get(member.position, None),
                             member.address,
                             member.email,
                             member.date_paid,
                             member.member_since,
                             member.date_expires])
    
    return response
    


