# Generated by Django 3.1.5 on 2021-01-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_auto_20210122_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reels_video',
            field=models.FileField(blank=True, upload_to='', verbose_name='Video Reels'),
        ),
    ]