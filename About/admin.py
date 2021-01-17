from django.contrib import admin
from .models import About
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_display = ['page_title', 'slug']
    list_display_link = ['page_title']
    search_fields = ['page_title', 'description', 'detail']

    class Meta:
        model = About


admin.site.register(About, AboutAdmin)
