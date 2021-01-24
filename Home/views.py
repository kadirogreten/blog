from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from Posts.models import *
from Posts.forms import NewsletterForm
from django.contrib import messages
from django.conf import settings
import requests
import urllib.request

# Create your views here.


def home(request):

    posts = Post.objects.all().order_by("-created_at")[:6]
    home_banner = Post.objects.filter(
        IsShowHome=True).exclude(hit_count_generic__hits=0).order_by('-hit_count_generic__hits')[:3]

    category_list = PostCategory.objects.filter(
        IsShowHome=True).order_by('row')[:5]

    popular_posts_slider = Post.objects.exclude(hit_count_generic__hits=0).order_by(
        '-hit_count_generic__hits')[:5]
    popular_posts = Post.objects.exclude(
        hit_count_generic__hits=0).order_by('-hit_count_generic__hits')[:15]
    get_reels = Post.objects.filter(
        post_type='R').order_by('-hit_count_generic__hits')[:15]

    get_stories = Post.objects.filter(
        post_type='S').order_by('-hit_count_generic__hits')[:15]

    newsletter_form = NewsletterForm(request.POST or None)
    if request.method == 'POST':

        if newsletter_form.is_valid():
            print('girdim')
            data = {
                'response': request.POST.get('g-recaptcha-response'),
                'secret': settings.RECAPTCHA_PRIVATE_KEY
            }
            print(data)
            resp = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result_json = resp.json()
            if result_json.get('success'):
                print(resp.json())
                newsletter = newsletter_form.save()
                messages.success(
                    request, 'Bültenimize başarılı bir şekilde kayıt oldunuz. Teşekkürler!')
                return HttpResponseRedirect('/')
            else:
                messages.error(
                    request, "Captcha Hatalı")
        else:
            messages.error(
                request, "Lütfen boş alanları doldurunuz!")

    context = {
        'posts': posts,
        'category_list': category_list,
        'home_banner': home_banner,
        'popular_posts': popular_posts,
        'popular_posts_slider': popular_posts_slider,
        'get_reels': get_reels,
        'get_stories': get_stories,
        'form': newsletter_form,
        'site_key': settings.RECAPTCHA_PUBLIC_KEY


    }

    print(popular_posts)
    return render(request, 'home/index.html', context)
