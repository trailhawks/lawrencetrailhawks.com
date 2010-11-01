from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.template import RequestContext
from lawrencetrailhawks.members.models import Member
from syncr.flickr.models import Photo
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_detail as obj_detail
from lawrencetrailhawks.members.forms import ContactForm
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


def officer_list(request):
    officers = Member.objects.filter(position__isnull=False)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "[Trailhawks]: %s" % form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = [officer.email for officer in officers]
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {
        'officers': officers,
        'form': form,
            },
        context_instance=RequestContext(request),
    )

        
