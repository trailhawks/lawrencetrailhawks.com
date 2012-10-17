from django.contrib import admin

from runs.models import Run, News


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class NewsInline(admin.StackedInline):
    model = News


class RunAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('day_of_week', 'name', 'run_time', )
    list_filter = ('day_of_week', 'run_time', )
    inlines = [NewsInline]

admin.site.register(Run, RunAdmin)
admin.site.register(News, NewsAdmin)
