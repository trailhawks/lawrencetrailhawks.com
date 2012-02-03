from django.contrib import admin
from reversion import VersionAdmin

from lawrencetrailhawks.races.models import EmergencyContact
from lawrencetrailhawks.races.models import News
from lawrencetrailhawks.races.models import Race
from lawrencetrailhawks.races.models import Racer
from lawrencetrailhawks.races.models import Registration
from lawrencetrailhawks.races.models import Report
from lawrencetrailhawks.races.models import Result


#class MemberInline(admin.TabularInline):
#    model = Race.contacts.through
#    #model = Member

class RegistrationInline(admin.TabularInline):
    model = Registration

class NewsInline(admin.StackedInline):
    model = News

class SponsorsInline(admin.TabularInline):
    model = Race.sponsors.through

class RegistrationAdmin(VersionAdmin):
    pass

class NewsAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title']}

class RaceAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title', 'annual']}
    list_display = ('title', 'annual', 'start_datetime')
    list_filter = ('start_datetime', 'annual',)
    ordering = ['-start_datetime']
    inlines = [RegistrationInline, NewsInline]
    #inlines = (SponsorsInline, RegistrationInline, NewsInline,)
    #inlines = [MemberInline, SponsorsInline, RegistrationInline, NewsInline]
    #inlines = [SponsorsInline, RegistrationInline, NewsInline]
    #exclude = ('sponsors',)

class ResultAdmin(VersionAdmin):
    list_display = ('time', 'racer', 'race', 'bib_number', 'place')
    list_filter = ('racer', 'race',)
    raw_id_fields = ('racer', 'race',)

class RacerAdmin(VersionAdmin):
    list_display = ('__unicode__', 'gender', 'email')
    list_filter = ('gender',)
    raw_id_fields = ('trailhawk',)
    search_fields = ('first_name', 'last_name', 'trailhawk__hawk_name',)  # removed 'trailhawk' field but this might be fixed in a later version of Django

class ReportAdmin(VersionAdmin):
    list_display = ('title', 'racer',)
    list_filter = ('racer',)

class EmergencyContactAdmin(VersionAdmin):
    pass

admin.site.register(Race, RaceAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
