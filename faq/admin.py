from django.contrib import admin

from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['question']}

admin.site.register(FAQ)
