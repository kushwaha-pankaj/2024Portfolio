from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'