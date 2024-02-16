from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Person

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        else:
            return 'No image'
    display_image.short_description = 'Image'

admin.site.register(Profile, ProfileAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'phone', 'email', 'address', 'freelancer', 'description')  # Fields to display in the list view
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        else:
            return 'No image'
    display_image.short_description = 'Image'

admin.site.register(Person, PersonAdmin)
