from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.links.models import Links
import datetime



def get_links(request):
	links = Links.objects.all()
	t = loader.get_template('links.html')
	c = Context({
		"links" : links,
	})
	
	return HttpResponse(t.render(c))
	
