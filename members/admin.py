from django.contrib import admin
from lawrencetrailhawks.members.models import Members

class MembersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','hawk_name', 'active', 'email', 'phone', 'date_paid')
    list_filter = ('active','date_paid')

admin.site.register(Members, MembersAdmin)