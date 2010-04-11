from django.contrib import admin
from lawrencetrailhawks.members.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','hawk_name', 'username', 'active', 'phone', 'date_paid')
    list_filter = ('active','date_paid')

admin.site.register(Member, MemberAdmin)