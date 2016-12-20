from django.contrib import admin

from .models import Run
from core.actions import disable_comments, enable_comments
from faq.admin import FaqInline
from news.admin import NewsInline


class RunAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['name', 'day_of_week', 'active', 'enable_comments', 'run_time']
    list_filter = ['enable_comments', 'day_of_week', 'run_time', 'location']
    raw_id_fields = ['contact']
    inlines = (
        NewsInline,
        FaqInline,
    )
    actions = [
        disable_comments,
        enable_comments
    ]


admin.site.register(Run, RunAdmin)
