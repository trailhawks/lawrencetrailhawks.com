from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Links


class LinksInline(generic.GenericStackedInline):
    model = Links
    extra = 0


class LinksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Links, LinksAdmin)
