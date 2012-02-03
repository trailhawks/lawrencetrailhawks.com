from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import Sponsor


class SponsorAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Sponsor, SponsorAdmin)
