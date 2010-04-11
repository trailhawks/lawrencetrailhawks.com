from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.members.models import Member
import datetime

def get_members(request):
    members = Member.objects.all()
    t = loader.get_template('members.html')
    c = Context({
        "members" : members,
    })
    
    return HttpResponse(t.render(c))
    
