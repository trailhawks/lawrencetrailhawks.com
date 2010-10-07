from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.sponsors.models import Sponsor
import datetime



def get_sponsors(request):
	sponsors = Sponsor.objects.active()
	t = loader.get_template('sponsors.html')
	c = Context({
		"sponsors" : sponsors,
	})
	
	return HttpResponse(t.render(c))
	
