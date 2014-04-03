from django.contrib import admin

from .models import Event
from core.actions import disable_comments, enable_comments
from faq.admin import FaqInline
from links.admin import LinksInline
from news.admin import NewsInline
from sponsors.admin import SponsorInline


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'enable_comments', 'status')
    list_filter = ('enable_comments', 'status')
    filter_horizontal = ('races',)
    save_on_top = True
    inlines = (
        FaqInline,
        NewsInline,
        LinksInline,
        SponsorInline,
    )
    actions = [
        disable_comments,
        enable_comments
    ]


admin.site.register(Event, EventAdmin)
