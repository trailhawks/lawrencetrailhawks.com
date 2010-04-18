from django.contrib import admin
from lawrencetrailhawks.events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('race',)
    list_filter = ('race', )

admin.site.register(Event, EventAdmin)
