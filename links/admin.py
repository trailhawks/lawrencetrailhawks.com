from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Links


class LinksInline(GenericStackedInline):
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
