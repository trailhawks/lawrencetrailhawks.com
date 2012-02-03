from django.contrib import admin
from reversion import VersionAdmin

from lawrencetrailhawks.members.models import Member


class MemberInline(admin.TabularInline):
    model = Member


class MemberAdmin(VersionAdmin):
    list_display = ('__unicode__', 'first_name', 'last_name', 'phone', 'date_paid', 'active')
    list_filter = ('date_paid', )
    search_fields = ('first_name', 'last_name')


admin.site.register(Member, MemberAdmin)
