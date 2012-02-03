from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import HawkNews


class HawkNewsAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'pub_date', 'draft')
    list_filter = ('pub_date', 'draft')

admin.site.register(HawkNews, HawkNewsAdmin)
