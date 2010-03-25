from django.contrib import admin
from lawrencetrailhawks.results.models import Race, Racer, Result, Report


class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['race_name', 'annual'] }
    list_display = ('race_name', 'annual', 'race_date', )
    list_filter = ('race_date', 'annual',)
    
class ResultAdmin(admin.ModelAdmin):
    list_display = ('race','racer', 'time')
    list_filter = ('race', 'racer',)
    
class RacerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender',)
    list_filter = ('gender',)
    
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'racer',)
    list_filter = ('racer',)


admin.site.register(Race, RaceAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Result,ResultAdmin)


