from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from lawrencetrailhawks.members.models import Member
import csv
import StringIO

@login_required
def member_list(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_list.csv'

    members = Member.objects.filter(active=True)
    member_list = csv.writer(response)

    for member in members:
        member_list.writerow([member.first_name,
                             member.hawk_name,
                             member.last_name,
                             member.date_paid,
                             member.member_since])
    
    return response
    


