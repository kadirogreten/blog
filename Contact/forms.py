from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'data-theme': 'light',
    }), label="")

    class Meta:
        model = Contact
        fields = [
            'name_surname',
            'email',
            'message',
        ]
