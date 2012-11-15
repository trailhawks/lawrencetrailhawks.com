from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import FAQ


class FaqInline(generic.GenericStackedInline):
    model = FAQ


class FaqAdmin(admin.ModelAdmin):
    pass


admin.site.register(FAQ, FaqAdmin)
