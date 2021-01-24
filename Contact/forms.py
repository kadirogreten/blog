from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name_surname',
            'email',
            'message',
        ]

        widgets = {
            'name_surname': forms.TextInput(attrs={'class': '', 'type': 'text', 'placeholder': 'Adınız Soyadınız', 'required': 'required', 'maxlength': '100'}),
            'email': forms.EmailInput(attrs={'class': '', 'type': 'text', 'placeholder': 'E-Posta Adresiniz', 'required': 'required', 'maxlength': '100'}),
            'message': forms.Textarea(attrs={'class': '', 'type': 'text', 'placeholder': 'Yorum Yaz', 'required': 'required', 'maxlength': '400'}),
        }

        def clean(self):
            cleaned_data = super(ContactForm, self).clean()
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            if not name and not email and not message:
                raise forms.ValidationError('You have to write something!')
