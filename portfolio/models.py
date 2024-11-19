from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def generate_unique_slug(instance):
    """
    Generate a unique slug for the instance based on its name.
    """
    slug = slugify(instance.name)
    existing_slugs = Category.objects.filter(slug__startswith=slug).exclude(id=instance.id)
    if existing_slugs.exists():
        slug = f"{slug}-{existing_slugs.count() + 1}"
    return slug


def pre_save_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)


pre_save.connect(pre_save_category_slug, sender=Category)


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'
