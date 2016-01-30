from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Links


class LinksInline(generic.GenericStackedInline):
    model = Links
    extra = 0


class LinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'object_id')
    fieldsets = (
        (None, {
            'fields': ('name', 'link', 'description')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('content_type', 'object_id')
        }),
    )


admin.site.register(Links, LinksAdmin)
