from django.contrib import admin

from members.models import Member


class MemberInline(admin.TabularInline):
    model = Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'first_name', 'last_name', 'phone', 'date_paid', 'active', 'receive_comment_emails')
    list_filter = ('date_paid', 'receive_comment_emails')
    search_fields = ('first_name', 'last_name')

admin.site.register(Member, MemberAdmin)
