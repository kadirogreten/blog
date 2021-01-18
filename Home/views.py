from django.shortcuts import render
from Posts.models import *

# Create your views here.


def home(request):
    try:
        posts = Post.objects.all()
        category_list = PostCategory.objects.all().order_by('-row')
        home_banner = Post.objects.filter(
            IsShowHome=True).exclude(hit_count_generic__hits=0).order_by('-hit_count_generic__hits')[:3]
        new_posts = Post.objects.all().order_by('-created_at')[:10]
        trending_posts = Post.objects.all()
        popular_posts_slider = Post.objects.order_by(
            '-hit_count_generic__hits')[:5]
        popular_posts = Post.objects.order_by('-hit_count_generic__hits')[:15]
        get_reels = Post.objects.filter(
            IsReelsVideo=True).order_by('-hit_count_generic__hits')[:3]

    except posts.DoesNotExist:
        posts = None

    context = {
        'posts': posts,
        'category_list': category_list,
        'home_banner': home_banner,
        'new_posts': new_posts,
        'trending_posts': trending_posts,
        'popular_posts': popular_posts,
        'popular_posts_slider': popular_posts_slider,
        'get_reels': get_reels


    }

    print(popular_posts)
    return render(request, 'home/index.html', context)
