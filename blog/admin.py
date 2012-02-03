from __future__ import absolute_import

from django.contrib import admin
from reversion import VersionAdmin

from .models import Post


class PostAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Post, PostAdmin)
