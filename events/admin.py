from django.contrib import admin
from lawrencetrailhawks.events.models import Event


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title', 'annual'] }
    list_display = ('title', 'annual', 'date',)
    list_filter = ('title', 'annual', 'date', )

admin.site.register(Event, EventAdmin)
