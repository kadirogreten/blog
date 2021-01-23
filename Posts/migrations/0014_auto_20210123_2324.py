# Generated by Django 3.1.5 on 2021-01-23 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0013_auto_20210123_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='title',
        ),
        migrations.RemoveField(
            model_name='posttags',
            name='IsShowHome',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcomment',
            name='name',
            field=models.CharField(default='dd', max_length=200, verbose_name='Adınız Soyadınız'),
            preserve_default=False,
        ),
    ]