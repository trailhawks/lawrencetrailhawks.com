from django.contrib import admin
from reversion import VersionAdmin

from lawrencetrailhawks.sponsors.models import Sponsor


class SponsorAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Sponsor, SponsorAdmin)
