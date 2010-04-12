from django.contrib import admin
from lawrencetrailhawks.results.models import Race, Racer, Result, Report


class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title', 'annual'] }
    list_display = ('title', 'annual', 'date', )
    list_filter = ('date', 'annual',)
    
class ResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'time', 'racer', 'bib_number', 'place')
    list_filter = ('race', 'racer')
    
class RacerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender',)
    list_filter = ('gender',)
    
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'racer',)
    list_filter = ('racer',)

admin.site.register(Race, RaceAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Result, ResultAdmin)


