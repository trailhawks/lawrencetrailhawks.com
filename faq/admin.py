from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import FAQ


class FaqInline(generic.GenericStackedInline):
    model = FAQ
    extra = 0


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'content_type', 'object_id')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('content_type', 'object_id')
        }),
    )


admin.site.register(FAQ, FaqAdmin)
