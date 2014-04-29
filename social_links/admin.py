from django.contrib import admin
from django.contrib.contenttypes import generic

from .forms import SocialLinkModelForm
from .models import SocialLink


class SocialLinkInline(generic.GenericStackedInline):
    model = SocialLink
    readonly_fields = ('remote_url', 'remote_id')
    extra = 0


class SocialLinkModelAdmin(admin.ModelAdmin):
    form = SocialLinkModelForm
    inlines = (
        SocialLinkInline,
    )
    abstract = True

    '''
    def get_form(self, request, obj=None, **kwargs):
        print obj, kwargs
        print type(obj)
        #self.form = SocialLinkModelForm
        admin_form = self.form()
        form = super(SocialLinkModelAdmin, self).get_form(request, obj=obj, **kwargs)
        #import ipdb
        #ipdb.set_trace()
        #fields = form.get_dynamic_fields(obj)
        #form.base_fields.update()
        return form
    '''

    '''
    def get_form(self, request, obj=None, **kwargs):
        admin_form = SocialLinkModelForm()
        fields = admin_form.get_dynamic_fields(obj)
        form = type('SocialLinkModelForm', (forms.ModelForm,), fields)
        return form
    '''

admin.site.register(SocialLink)
