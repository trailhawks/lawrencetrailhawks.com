
def enable_comments(modeladmin, request, queryset):
    queryset.update(enable_comments=True)

enable_comments.short_description = 'Enable comments'


def disable_comments(modeladmin, request, queryset):
    queryset.update(enable_comments=False)

disable_comments.short_description = 'Disable comments'
