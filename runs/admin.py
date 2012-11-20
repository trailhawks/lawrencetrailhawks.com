from django.contrib import admin

from .models import Run
from faq.admin import FaqInline
from news.admin import NewsInline


class RunAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('day_of_week', 'name', 'run_time', )
    list_filter = ('day_of_week', 'run_time', )
    inlines = (
        NewsInline,
        FaqInline,
    )

admin.site.register(Run, RunAdmin)
