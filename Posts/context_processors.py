from .models import *


def post_category_nav(request):
    return {
        'post_category': PostCategory.objects.filter(IsShowMenu=True)[:4]
    }
