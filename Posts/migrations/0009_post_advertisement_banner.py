# Generated by Django 3.1.5 on 2021-01-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0008_postcategory_isshowhome'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='advertisement_banner',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Reklam Resmi'),
        ),
    ]