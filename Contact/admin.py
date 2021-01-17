from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'email', 'message_date']
    list_display_link = ['name_surname', 'email', 'message_date']
    search_fields = ['name_surname', 'email']

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
