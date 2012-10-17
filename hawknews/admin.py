from django.contrib import admin

from hawknews.models import HawkNews


class HawkNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'pub_date', 'status')
    list_filter = ('pub_date', 'status')

admin.site.register(HawkNews, HawkNewsAdmin)
