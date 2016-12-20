import csv

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import ContactForm
from .models import Member, Term
from races.models import Race
from runs.models import Run


class MemberDetailView(DetailView):
    model = Member
    navitem = 'members'


class MemberEmailPreview(TemplateView):
    template_name = 'emails/renewal.html'

    def get_context_data(self):
        context = super(MemberEmailPreview, self).get_context_data()
        context['first_name'] = 'Trailhawks'
        context['expire_date'] = datetime.now()
        return context


class MemberListView(ListView):
    queryset = Member.objects.current()
    navitem = 'members'

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context['current_officers'] = Term.objects.current().order_by('office__order')
        context['previous_officers'] = Term.objects.previous().order_by('office__order')
        context['run_leaders'] = Run.objects.active()
        context['race_leaders'] = Race.objects.all()
        return context


def officer_list(request):
    officer_ids = Term.objects.current().values_list('member__id', flat=True)
    officers = Member.objects.filter(id__in=officer_ids)

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

    return render_to_response('contact.html',
                              {'form': form},
                              context_instance=RequestContext(request))


class MemberExport(TemplateView):
    content_type = 'text/csv'


@login_required
def member_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_list.csv'
    current_site = Site.objects.get_current()

    members = Member.objects.all().order_by('-date_paid')
    member_list = csv.writer(response)
    member_list.writerow(['id',
                         'First Name',
                         'Hawk Name',
                         'Last Name',
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
                         'Dues Due',
                         'Website Admin Url'])

    for member in members:
        member_list.writerow([member.id,
                             member.first_name,
                             '"{}"'.format(member.hawk_name),
                             member.last_name,
                             member.get_gender_display(),
                             #member.get_position(),
                             '',
                             member.address,
                             member.address2,
                             member.city,
                             member.state,
                             member.zip,
                             member.email,
                             member.date_paid,
                             member.member_since,
                             member.date_expires,
                             'http://' + current_site.domain + reverse('admin:members_member_change', args=[member.pk])])

    return response
