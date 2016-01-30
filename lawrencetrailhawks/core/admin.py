from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist


class BaseMetadataAdmin(admin.ModelAdmin):
    """Base admin class for generic content."""
    readonly_fields = ('updated_user', 'updated', 'created_user', 'created')

    def save_model(self, request, obj, form, change):
        try:
            obj.created_user
        except ObjectDoesNotExist:
            obj.created_user = request.user

        obj.updated_user = request.user
        super(BaseMetadataAdmin, self).save_model(request, obj, form, change)
