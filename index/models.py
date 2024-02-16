from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
        

class Person(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='person')
    image = models.ImageField(upload_to='person_images/')
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    freelancer = models.BooleanField(default=True)  # Assuming this indicates availability

    def __str__(self):
        return self.profile.name
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Person"

