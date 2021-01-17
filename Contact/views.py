from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact_view(request):

    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        contact = contact_form.save()
        messages.success(request, 'Mesajınız başarılı bir şekilde iletildi!')
        return HttpResponseRedirect(contact.get_absolute_url())

    context = {
        'form': contact_form,
    }

    return render(request, 'kurumsal/contact.html', context)
