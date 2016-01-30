from django.contrib import admin
from django.contrib.contenttypes import generic

from .models import News
from core.actions import disable_comments, enable_comments


class NewsInline(generic.GenericStackedInline):
    model = News
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'pub_date', 'enable_comments', 'status', 'content_type', 'object_id']
    list_filter = ['enable_comments', 'pub_date', 'status']
    actions = [
        disable_comments,
        enable_comments
    ]
    fieldsets = (
        (None, {
            'fields': ('pub_date', 'title', 'slug', 'body', 'status', 'alert_status', 'enable_comments')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('content_type', 'object_id')
        }),
    )


admin.site.register(News, NewsAdmin)
