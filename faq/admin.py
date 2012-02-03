from django.contrib import admin
from reversion import VersionAdmin

from lawrencetrailhawks.faq.models import FAQ


class FAQAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['question']}

admin.site.register(FAQ)
