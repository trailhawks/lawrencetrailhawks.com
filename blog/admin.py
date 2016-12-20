from django.contrib import admin

from .models import Post
from core.actions import disable_comments, enable_comments


class PostAdmin(admin.ModelAdmin):
    ordering = ['-publish']
    list_display = ('title', 'status', 'enable_comments', 'author', 'publish')
    list_filter = ('enable_comments', 'status', 'publish')
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ('author',)
    search_fields = ('title', 'tease', 'body')
    actions = [
        disable_comments,
        enable_comments
    ]


admin.site.register(Post, PostAdmin)
