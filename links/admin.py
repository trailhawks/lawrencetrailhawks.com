from django.contrib import admin
from reversion import VersionAdmin

from lawrencetrailhawks.links.models import Links


class LinkAdmin(VersionAdmin):
    pass

admin.site.register(Links, LinkAdmin)
