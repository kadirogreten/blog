from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

import requests
from django.conf import settings

# Create your views here.


def contact_view(request):

    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        data = {
            'response': request.POST.get('g-recaptcha-response'),
            'secret': settings.RECAPTCHA_PRIVATE_KEY
        }
        resp = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result_json = resp.json()
        if result_json.get('success'):
            contact = contact_form.save()
            messages.success(
                request, 'Mesajınız başarılı bir şekilde iletildi!')
            return HttpResponseRedirect(contact.get_absolute_url())
        else:
            messages.error(
                request, "Captcha Hatalı")

    context = {
        'form': contact_form,
        'site_key': settings.RECAPTCHA_PUBLIC_KEY
    }

    return render(request, 'kurumsal/contact.html', context)
