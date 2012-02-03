from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import News
from .models import Run


class NewsAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title']}


class NewsInline(admin.StackedInline):
    model = News

class RunAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('order', 'run_date', 'name', 'run_time',)
    list_filter = ('run_date', 'run_time',)
    inlines = [NewsInline]


admin.site.register(Run, RunAdmin)
admin.site.register(News, NewsAdmin)
