from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.members.models import Member
from syncr.flickr.models import Photo
import datetime

def get_members(request):
    members = Member.objects.all()
    t = loader.get_template('members.html')
    c = Context({
        "members" : members,
    })
    
    return HttpResponse(t.render(c))
    
def member_detail(request, object_id, queryset):
    person = Member.objects.get(pk=object_id)
    photos = Photo.objects.filter(tags__icontains=person.first_name).filter(tags__icontains=person.last_name).order_by('?')[0:7]
    return obj_detail(request,
                         queryset= queryset,
                         object_id = object_id,
                         extra_context= {'photos': photos}
                         )
    
