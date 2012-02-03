from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import FAQ


class FAQAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['question']}

admin.site.register(FAQ)
