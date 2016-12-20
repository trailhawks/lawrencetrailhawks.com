from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import FAQ


class FaqInline(generic.GenericStackedInline):
    model = FAQ
    extra = 0


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'content_type', 'get_object_name')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('content_type', 'object_id')
        }),
    )

    def get_object_name(self, obj):
        if obj.content_object and len(unicode(obj.content_object)):
            return obj.content_object
    get_object_name.short_description = 'associated object'


admin.site.register(FAQ, FaqAdmin)
