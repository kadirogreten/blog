from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from .models import *
from django.utils.text import slugify
from hitcount.views import HitCountDetailView
import hitcount  # import entire package
from hitcount.models import HitCount

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


def category_list(request):
    category_list = PostCategory.objects.all().order_by('-row')
    return render(request, 'hosting/hosting.html', {'category_list': category_list})


def get_all_posts(request):
    category = PostCategory.objects.all().order_by('-row')
    return render(request, 'hosting/hosting.html', {'category_list': category_list})


def post_list(request, slug):
    category = get_object_or_404(PostCategory, slug=slug)
    print(category)
    product_list = Post.objects.filter(categories=category)

    context = {
        'category': category,
        'product_list': product_list,

    }
    return render(request, 'post/posts.html', context)


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
# mark it
    hit_count = HitCount.objects.get_for_object(post)
    hit_count_response = hitcount.views.HitCountMixin.hit_count(
        request, hit_count)

    # count the views
    post_views = post.hit_count.hits
    print(post)
    if not post.title:
        return render(request, 'hosting/404.html', {})
    # print(all_fields)
    context = {
        'categories': post.categories,
        'post': post,
        'post_views': post_views

    }
    return render(request, 'post/post_detail.html', context)
