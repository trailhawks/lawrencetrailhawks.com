from django.contrib import admin

from .models import EmergencyContact, Race, Racer, RaceType, Registration, Report, Result
from faq.admin import FaqInline
from news.admin import NewsInline
from sponsors.admin import SponsorInline


class RaceDirectorInline(admin.StackedInline):
    model = Race.race_directors.through
    raw_id_fields = ('member',)


class RegistrationInline(admin.TabularInline):
    model = Registration


class RegistrationAdmin(admin.ModelAdmin):
    pass


class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title', 'annual']}
    list_display = ('title', 'annual', 'start_datetime')
    list_filter = ('start_datetime', 'annual', )
    ordering = ['-start_datetime']
    inlines = (
        RaceDirectorInline,
        RegistrationInline,
        SponsorInline,
        NewsInline,
        FaqInline,
    )
    exclude = ('race_directors', 'sponsors',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('race', 'race_type', 'racer', 'time', 'place', 'course_record', 'dns', 'dnf', 'dq')
    list_filter = ('race_type', 'course_record', 'dns', 'dnf', 'dq', 'race')
    raw_id_fields = ('racer', 'race')
    search_fields = ('time', 'place')


class RacerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'gender', 'email', 'trailhawk')
    list_filter = ('gender', )
    raw_id_fields = ('trailhawk', 'contact')
    search_fields = ('first_name', 'last_name')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'racer', )
    list_filter = ('racer', )


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
admin.site.register(EmergencyContact, EmergencyContactAdmin)
