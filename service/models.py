from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

