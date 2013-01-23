from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import News


class NewsInline(generic.GenericStackedInline):
    model = News
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'pub_date', 'status')
    list_filter = ('pub_date', 'status')

admin.site.register(News, NewsAdmin)
