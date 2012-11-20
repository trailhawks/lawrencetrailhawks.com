from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Links


class LinksInline(generic.GenericStackedInline):
    model = Links


admin.site.register(Links)
