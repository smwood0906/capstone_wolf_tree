from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_zip = forms.CharField(required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name "
        self.fields['contact_email'].label = "Your email "
        self.fields['contact_zip'].label = "Your zip code (optional) "
        self.fields['content'].label =  "Your message"