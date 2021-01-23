from django.db import models
from django.urls import reverse

# Create your models here.


class Contact(models.Model):
    name_surname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    message_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("contact:contact")

    class Meta:
        ordering = ['-message_date', 'id']
        verbose_name_plural = "İletişim"


class Newsletter(models.Model):
    email = models.EmailField()
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-message_date', 'id']
        verbose_name_plural = "Bültenimize Katılın"
