from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextFormField, RichTextField
import hitcount
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


class PostCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kategori Adı")
    row = models.IntegerField(
        unique=True, editable=True, verbose_name="Kategori Sırası")
    slug = models.SlugField(
        unique=True, verbose_name="Post Kategorisi urlsi", max_length=250, editable=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    created_at = models.DateTimeField(
        verbose_name="Oluşturulma Zamanı", auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:category_detail", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while PostCategory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(PostCategory, self).save(*args, **kwargs)

    class Meta:
        ordering = ['row', 'id']
        verbose_name_plural = "Post Kategorileri"


class Post(models.Model, HitCountMixin):
    categories = models.ManyToManyField(
        PostCategory, verbose_name="Kategori Seç", related_name="post")
    title = models.CharField(max_length=200, verbose_name="Post Başlığı")
    slug = models.SlugField(
        unique=True, verbose_name="Post urlsi", max_length=350, editable=False)
    author = models.CharField(max_length=200, verbose_name="Yazar")
    row = models.IntegerField(
        unique=True, verbose_name="Post Sırası", editable=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    product_image = models.ImageField(
        verbose_name="Post Resmi", name="post_image")
    reels_video = models.FileField(
        verbose_name="Video Reels", name="reels_video", null=True)
    detail = RichTextUploadingField(verbose_name="Post Detayı")
    created_at = models.DateTimeField(
        verbose_name="Oluşturulma Zamanı", auto_now_add=True)
    IsShowHome = models.BooleanField(
        verbose_name="Anasayfada Göster", default=False)
    IsShowTopSlider = models.BooleanField(
        verbose_name="Anasayfada Üst Slider Göster", default=False)
    IsShowMidSlider = models.BooleanField(
        verbose_name="Anasayfada Orta Slider Göster", default=False)
    IsReelsVideo = models.BooleanField(
        verbose_name="Reels Göster", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(
            f"{self.title.replace('ı', 'i')}")
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Post.objects.get(pk=self.pk).title
            if self.title == orig:
                return super(Post, self).save(*args, **kwargs)
            else:
                self.slug = self.get_unique_slug()
                return super(Post, self).save(*args, **kwargs)
        else:
            self.slug = self.get_unique_slug()
            return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at', 'id']
        verbose_name_plural = "Posts"


class PostComment(models.Model):
    post = models.ForeignKey(
        'Post', verbose_name="Post Seç", related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Post Başlığı")
    detail = RichTextField(verbose_name="Yorum")
    created_at = models.DateTimeField(
        verbose_name="Oluşturulma Zamanı", auto_now_add=True)
    IsShowHome = models.BooleanField(
        verbose_name="Onayla Göster", default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', 'id']
        verbose_name_plural = "Post Yorumları"
