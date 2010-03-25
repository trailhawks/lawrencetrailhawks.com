from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.faq.models import FAQ
import datetime



def get_faq_list(request):
	faq_list = FAQ.objects.all()
	t = loader.get_template('faq.html')
	c = Context({
		"faq_list" : faq_list,
	})
	
	return HttpResponse(t.render(c))
	
