from django.shortcuts import render
from Posts.models import *

# Create your views here.


def home(request):
    try:
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

    except posts.DoesNotExist:
        posts = None

    context = {
        'posts': posts,
        'category_list': category_list,
        'home_banner': home_banner,
        'popular_posts': popular_posts,
        'popular_posts_slider': popular_posts_slider,
        'get_reels': get_reels,
        'get_stories': get_stories


    }

    print(popular_posts)
    return render(request, 'home/index.html', context)
