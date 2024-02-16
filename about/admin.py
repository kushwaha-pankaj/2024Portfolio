from django.contrib import admin
from .models import About, Testimonial

class AboutAdmin(admin.ModelAdmin):
    list_display = ('i_am', 'based_in', 'projects_completed', 'cups_of_coffee', 'satisfied_clients', 'total_certificate', 'years_of_experience')

admin.site.register(About, AboutAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_position')

admin.site.register(Testimonial, TestimonialAdmin)
