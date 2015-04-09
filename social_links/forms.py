from django import forms


class SocialLinkModelForm(forms.ModelForm):
    post_to_twitter = forms.BooleanField(
        label='Post to Twitter?',
        widget=forms.RadioSelect(choices=((True, 'Yes'), (False, 'No'))),
        initial=True,
        required=False,
        help_text='Your message will be sent 10 to 15 minutes from when you save.'
    )

    def get_dynamic_fields(self, obj):
        fields = {}
        for bit in range(0, 2):
            bit_key = 'bit_{0}'.format(bit)
            field = forms.CharField(
                label=bit_key,
                required=False,
                help_text='bit.help_text',
                #widget=CKEditorWidget(),
                #initial=bit.data.data,
            )
            fields[bit_key] = field

        return fields

    #def save_formset(self, request, form, formset, change):
    #    print 'save_formset'
    #    return super(SocialLinkModelForm, self).save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change):
        print 'save_model'
        print form.cleaned_data['post_to_twitter']

        if change and form.cleaned_data['post_to_twitter']:
            print 'fire off signal to post to twitter...'

        return super(SocialLinkModelForm, self).save_model(request, obj, form, change)
