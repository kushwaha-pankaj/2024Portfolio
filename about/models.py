from django.db import models

class About(models.Model):
    i_am = models.CharField(max_length=20)
    based_in = models.CharField(max_length=100)
    description_one = models.TextField()
    description_two = models.TextField()
    signature_image = models.ImageField(upload_to='about/signatures/')
    projects_completed = models.PositiveIntegerField(default=0)
    cups_of_coffee = models.PositiveIntegerField(default=0)
    satisfied_clients = models.PositiveIntegerField(default=0)
    total_certificate = models.PositiveIntegerField(default=0)
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'About - {self.i_am}'

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        
from django.db import models

class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    feedback = models.TextField()

    def __str__(self):
        return self.author_name
