from django.contrib import admin
from lawrencetrailhawks.hawknews.models import HawkNews

class HawkNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
    list_display = ('title', 'pub_date', 'draft')
    list_filter = ('pub_date', 'draft')

admin.site.register(HawkNews, HawkNewsAdmin)