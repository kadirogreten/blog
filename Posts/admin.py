from django.contrib import admin

from Posts.models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'slug']
    list_display_link = ['title']
    search_fields = ['title', 'detail']

    class Meta:
        model = PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    list_display_link = ['title']
    search_fields = ['title', ]

    class Meta:
        model = Post


class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_link = ['name', 'email']
    search_fields = ['name', 'email', ]

    class Meta:
        model = PostComment


class PostTagsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_link = ['title', ]
    search_fields = ['title', ]

    class Meta:
        model = PostTags


admin.site.register(PostCategory, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentsAdmin)
admin.site.register(PostTags, PostTagsAdmin)
