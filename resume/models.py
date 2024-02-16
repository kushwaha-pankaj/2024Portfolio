from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MaxValueValidator

class Education(models.Model):
    course_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True)

    def __str__(self):
        return self.course_name

class Experience(models.Model):
    WORK_MODE_CHOICES = [
        ('Freelancer', 'Freelancer'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Personal Project', 'Personal Project'),
    ]

    WORK_LOCATION_CHOICES = [
        ('In office', 'In office'),
        ('Remotely', 'Remotely'),
        ('Hybrid', 'Hybrid'),
    ]

    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    start_date = models.CharField(("Start Date"), max_length=50, blank=True, null=True)
    end_date = models.CharField(("End Date"), max_length=50, blank=True, null=True)
    mode_of_work = models.CharField(max_length=50, choices=WORK_MODE_CHOICES)
    work_location = models.CharField(max_length=50, choices=WORK_LOCATION_CHOICES)
    description = CKEditor5Field(blank=True, null=True)
    experience_letter = models.FileField(upload_to='experience_letters/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"



class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name

class NonTechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name
