from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from .models import *
from django.utils.text import slugify
from hitcount.views import HitCountDetailView
import hitcount  # import entire package
from hitcount.models import HitCount
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings

from .forms import NewsletterForm, CommetForm

from django.contrib import messages

import requests

# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = 'post/post_detail.html'
#     context_object_name = 'post'
#     slug_field = 'slug'
#     # set to True to count the hit
#     count_hit = True

#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         context.update({
#             'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
#         })
#         return context


def post_list(request):
    page = request.GET.get('page', 1)
    post_list = Post.objects.all().order_by('-row')
    categories = PostCategory.objects.all().order_by("row")
    paginator = Paginator(post_list, 6)
    latest_post = Post.objects.all().order_by("-created_at")[:4]

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/posts.html', {
        'post_list': posts,
        'categories': categories,
        'latest_post': latest_post
    })


def category_list(request, slug):
    category = get_object_or_404(PostCategory, slug=slug)
    hit_count = HitCount.objects.get_for_object(category)

    hit_count_response = hitcount.views.HitCountMixin.hit_count(
        request, hit_count)

    # count the views

    categories = PostCategory.objects.all().order_by("row")
    page = request.GET.get('page', 1)
    product_list = Post.objects.filter(categories=category).order_by("row")
    paginator = Paginator(product_list, 1)
    latest_post = Post.objects.all().order_by("-created_at")[:4]
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print(category)
    context = {
        'category': category,
        'posts': posts,
        'categories': categories,
        'latest_post': latest_post

    }
    return render(request, 'post/categories.html', context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
# mark it
    hit_count = HitCount.objects.get_for_object(post)

    hit_count_response = hitcount.views.HitCountMixin.hit_count(
        request, hit_count)

    # count the views
    post_views = post.hit_count.hits

    post_comments = PostComment.objects.filter(post=post)

    commet_form = CommetForm(request.POST or None)
    if request.method == 'POST':

        if commet_form.is_valid():
            data = {
                'response': request.POST.get('g-recaptcha-response'),
                'secret': settings.RECAPTCHA_PRIVATE_KEY
            }
            resp = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result_json = resp.json()
            if result_json.get('success'):
                print('girdim')
                commet_form.post = post
                commet = commet_form.save()
                messages.success(
                    request, 'Yorumunuz başarılı bir şekilde iletildi!')
                return HttpResponseRedirect(commet.post.get_absolute_url())
            else:
                messages.error(
                    request, "Captcha Hatalı")
        else:
            messages.error(
                request, "Lütfen boş alanları doldurunuz! Ya da captcha işaretleyiniz")

    if not post.title:
        return render(request, 'post/404.html', {})
    # print(all_fields)
    context = {
        'categories': post.categories,
        'post': post,
        'post_views': post_views,
        'post_comments': post_comments,
        'form': commet_form,
        'site_key': settings.RECAPTCHA_PUBLIC_KEY


    }
    return render(request, 'post/post_detail.html', context)
