from django import forms
from Contact.models import Newsletter

from .models import PostComment
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.helper import FormHelper


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': '', 'type': 'text', 'placeholder': 'E-Posta Adresiniz', 'required': 'required', 'maxlength': '100'}),
        }

        def clean(self):
            cleaned_data = super(NewsletterForm, self).clean()
            email = cleaned_data.get('email')
            if not email:
                raise forms.ValidationError('You have to write something!')


class CommetForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = [
            'post',
            'name',
            'email',
            'detail'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact-form__input-text', 'type': 'text', 'placeholder': 'Adınız Soyadınız', 'required': 'required', 'maxlength': '100'}),
            'email': forms.EmailInput(attrs={'class': 'contact-form__input-text', 'type': 'text', 'placeholder': 'E-Posta Adresiniz', 'required': 'required', 'maxlength': '100'}),
            'detail': forms.Textarea(attrs={'class': 'contact-form__textarea', 'type': 'text', 'placeholder': 'Yorum Yaz', 'required': 'required', 'maxlength': '400'}),
        }
        post = forms.CharField(       # A hidden input for internal use
            max_length=50,              # tell from which page the user sent the message
            widget=forms.HiddenInput()
        )

    def clean(self):
        cleaned_data = super(CommetForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        detail = cleaned_data.get('detail')
        if not name and not email and not detail:
            raise forms.ValidationError('You have to write something!')
