from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Sponsor


class SponsorInline(generic.GenericStackedInline):
    model = Sponsor


class SponsorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Sponsor, SponsorAdmin)
