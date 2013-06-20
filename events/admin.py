from django.contrib import admin

from .models import Event
from faq.admin import FaqInline
from links.admin import LinksInline
from news.admin import NewsInline
from sponsors.admin import SponsorInline


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'status')
    list_filter = ('status', )
    filter_horizontal = ('races',)
    save_on_top = True
    inlines = (
        FaqInline,
        NewsInline,
        LinksInline,
        SponsorInline,
    )


admin.site.register(Event, EventAdmin)
