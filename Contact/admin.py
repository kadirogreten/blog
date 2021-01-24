from django.contrib import admin
from .models import Contact, Newsletter

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'email', 'message_date']
    list_display_link = ['name_surname', 'email', 'message_date']
    search_fields = ['name_surname', 'email']

    class Meta:
        model = Contact


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'message_date']
    list_display_link = ['email', 'message_date']
    search_fields = ['email']

    class Meta:
        model = Newsletter


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
