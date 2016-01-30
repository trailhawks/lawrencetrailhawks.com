from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import Sponsor


class SponsorInline(generic.GenericStackedInline):
    model = Sponsor
    extra = 0


class SponsorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'active', 'homepage', 'content_type', 'object_id')
    list_filter = ('active', 'homepage',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'active', 'homepage', 'url', 'address', 'phone', 'email', 'logo', 'discount_detail')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('content_type', 'object_id')
        }),
    )


admin.site.register(Sponsor, SponsorAdmin)
