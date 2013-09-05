import csv

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ContactForm
from .models import Member


class MemberDetailView(DetailView):
    model = Member


class MemberListView(ListView):
    queryset = Member.active_objects.all()


def officer_list(request):
    officers = Member.objects.filter(position__isnull=False).order_by('position')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = '[Trailhawks]: %s' % form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = [officer.email for officer in officers]
            if cc_myself:
                recipients.append(sender)

            message_html = loader.render_to_string('emails/contact_message.html', {'body': message, 'sender': sender, 'subject': subject})
            message_text = loader.render_to_string('emails/contact_message.txt', {'body': message, 'sender': sender, 'subject': subject})

            msg = EmailMultiAlternatives(subject, message_text, 'no-reply@lawrencetrailhawks.com', recipients)
            msg.attach_alternative(message_html, 'text/html')
            msg.send()

            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()

    return render_to_response('contact.html', {
        'officers': officers,
        'form': form,
            },
        context_instance=RequestContext(request),
    )


@login_required
def member_list(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_list.csv'

    members = Member.active_objects.all().order_by('-date_paid')
    member_list = csv.writer(response)
    member_list.writerow(['First Name',
                         'Last Name',
                         'Hawk Name',
                         'Gender',
                         'Club Officer Title',
                         'Address',
                         'Address2',
                         'City',
                         'State',
                         'Zip',
                         'Email Address',
                         'Date paid',
                         'Member Since',
                         'Dues Due'])

    for member in members:
        member_list.writerow([member.first_name,
                             member.last_name,
                             member.hawk_name,
                             member.get_gender_display(),
                             member.get_position_display(),
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
