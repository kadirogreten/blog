# Generated by Django 3.1.5 on 2021-01-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0011_posttags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='Posts.PostTags', verbose_name='Etiket Seç'),
        ),
    ]
