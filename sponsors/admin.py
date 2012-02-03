from django.contrib import admin

from lawrencetrailhawks.sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Sponsor, SponsorAdmin)
