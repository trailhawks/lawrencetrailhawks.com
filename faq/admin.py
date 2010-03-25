from django.contrib import admin
from lawrencetrailhawks.faq.models import FAQ

class FAQAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['question'] }

admin.site.register(FAQ)