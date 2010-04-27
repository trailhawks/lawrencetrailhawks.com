from django.contrib import admin
from lawrencetrailhawks.races.models import Race, Racer, Result, Report, Registration, News, EmergencyContact

class RegistrationInline(admin.TabularInline):
    model = Registration

class NewsInline(admin.StackedInline):
    model = News
        
class RegistrationAdmin(admin.ModelAdmin):
    pass
    
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title',] }
    
class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title', 'annual'] }
    list_display = ('title', 'annual', 'start_datetime', )
    list_filter = ('start_datetime', 'annual',)
    inlines = (RegistrationInline, NewsInline,)
    
class ResultAdmin(admin.ModelAdmin):
    list_display = ('time', 'racer', 'race', 'bib_number', 'place')
    list_filter = ('racer', 'race',)
    
class RacerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'gender', 'email', )
    list_filter = ('gender',)
    
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'racer',)
    list_filter = ('racer',)
    
class EmergencyContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Race, RaceAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
