from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class About(models.Model):
    page_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    banner_image = models.ImageField(
        verbose_name="Banner Image", name="BannerImage")
    detail = RichTextUploadingField()
    slug = models.SlugField(unique=True, max_length=250, editable=False)

    def __str__(self):
        return self.page_title

    def get_absolute_url(self):
        return reverse("about:detail", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(self.page_title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while About.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if self.pk:
            orig = About.objects.get(pk=self.pk).page_title
            if self.page_title == orig:
                return super(About, self).save(*args, **kwargs)
            else:
                self.slug = self.get_unique_slug()
                return super(About, self).save(*args, **kwargs)
        else:
            self.slug = self.get_unique_slug()
            return super(About, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-page_title', 'id']
        verbose_name_plural = "Hakkımızda"
