from django.contrib import admin
from lawrencetrailhawks.events.models import Event


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title', 'date',)
    list_filter = ('title', 'date', )

admin.site.register(Event, EventAdmin)
