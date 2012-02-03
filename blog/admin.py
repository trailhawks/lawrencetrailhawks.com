from reversion import VersionAdmin
from django.contrib import admin

from blog.models import Post


class PostAdmin(VersionAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Post, PostAdmin)
