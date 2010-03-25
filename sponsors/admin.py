from django.contrib import admin
from lawrencetrailhawks.sponsors.models import Sponsors

class SponsorsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }

admin.site.register(Sponsors, SponsorsAdmin)