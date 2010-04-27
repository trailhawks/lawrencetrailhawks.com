from django.contrib import admin
from lawrencetrailhawks.runs.models import Run, News

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

class NewsInline(admin.StackedInline):
    model = News

class RunAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['name'] }
    list_display = ('run_date', 'name', 'run_time',)
    list_filter = ('run_date', 'run_time',)
    inlines = [NewsInline,]

admin.site.register(Run, RunAdmin)
admin.site.register(News, NewsAdmin)