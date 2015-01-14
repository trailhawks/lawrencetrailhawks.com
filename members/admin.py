from django.contrib import admin

from .models import Member, Office, Term


class MemberInline(admin.TabularInline):
    model = Member
    extra = 0


class TermInline(admin.TabularInline):
    model = Term
    extra = 0


class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'last_name', 'phone', 'date_paid', 'active', 'receive_comment_emails')
    list_filter = ('date_paid', 'receive_comment_emails')
    list_per_page = 300
    ordering = ['last_name', 'first_name']
    search_fields = ('first_name', 'last_name')
    inlines = [
        TermInline,
    ]


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    prepopulated_fields = {'slug': ['name']}
    ordering = ['order']


class TermAdmin(admin.ModelAdmin):
    list_display = ('member', 'office', 'start', 'end')
    list_filter = ['office']
    raw_id_fields = ['member']
    ordering = ['-start', '-end']


admin.site.register(Member, MemberAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Term, TermAdmin)
