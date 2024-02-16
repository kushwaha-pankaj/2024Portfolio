from django.contrib import admin
from .models import BlogPost, Tag, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'is_published', 'display_image']
    list_filter = ['publish_date', 'is_published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}  # Prepopulated slug field based on title
    date_hierarchy = 'publish_date'
    filter_horizontal = ('tags', 'categories')

    def display_image(self, obj):
        return obj.image.url if obj.image else ''
    display_image.short_description = 'Image'

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
from django.contrib import admin
from django.utils.text import slugify
from .models import BlogPost, Tag, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Prepopulate slug field based on name

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

admin.site.register(Category, CategoryAdmin)

