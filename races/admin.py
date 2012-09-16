from django.contrib import admin

from lawrencetrailhawks.races.models import EmergencyContact
from lawrencetrailhawks.races.models import News
from lawrencetrailhawks.races.models import Race
from lawrencetrailhawks.races.models import Racer
from lawrencetrailhawks.races.models import RaceType
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


class RegistrationAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title', 'annual']}
    list_display = ('title', 'annual', 'start_datetime')
    list_filter = ('start_datetime', 'annual',)
    ordering = ['-start_datetime']
    inlines = (SponsorsInline, RegistrationInline, NewsInline,)
    #inlines = [MemberInline, SponsorsInline, RegistrationInline, NewsInline]
    #inlines = [SponsorsInline, RegistrationInline, NewsInline]
    exclude = ('sponsors',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('time', 'racer', 'race', 'race_type', 'bib_number', 'place')
    list_filter = ('race', 'race_type')
    raw_id_fields = ('racer', 'race')


class RacerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'gender', 'email')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'racer',)
    list_filter = ('racer',)


class EmergencyContactAdmin(admin.ModelAdmin):
    pass


class RaceTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Race, RaceAdmin)
admin.site.register(RaceType, RaceTypeAdmin)
admin.site.register(Racer, RacerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
