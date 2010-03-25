from django.contrib import admin
from lawrencetrailhawks.runs.models import Runs

class RunsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    list_display = ('run_date', 'name', 'run_time',)
    list_filter = ('run_date', 'run_time',)

admin.site.register(Runs, RunsAdmin)