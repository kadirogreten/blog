from django import forms
from Contact.models import Newsletter
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.helper import FormHelper


class NewsletterForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'data-theme': 'light',
    }), label="")

    class Meta:
        model = Newsletter
        fields = [
            'email',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': '', 'type': 'text'}),
        }
