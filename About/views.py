from django.shortcuts import render, get_object_or_404
from .models import About
from django.utils.text import slugify
# Create your views here.


def about_detail(request, slug):
    about = get_object_or_404(About, slug=slug)
    context = {
        'about': about
    }

    return render(request, 'kurumsal/about.html',  context)
