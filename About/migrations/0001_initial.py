# Generated by Django 3.1.5 on 2021-01-17 18:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('BannerImage', models.ImageField(upload_to='', verbose_name='Banner Image')),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Hakkımızda',
                'ordering': ['-page_title', 'id'],
            },
        ),
    ]
