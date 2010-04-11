from django.contrib import admin
from lawrencetrailhawks.runs.models import Run

class RunAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    list_display = ('run_date', 'name', 'run_time',)
    list_filter = ('run_date', 'run_time',)

admin.site.register(Run, RunAdmin)