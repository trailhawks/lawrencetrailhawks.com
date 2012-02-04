from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import Links


class LinkAdmin(VersionAdmin):
    pass

admin.site.register(Links, LinkAdmin)
