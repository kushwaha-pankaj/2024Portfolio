from django.contrib import admin
from .models import Education, Experience, TechnicalSkill, NonTechnicalSkill

class EducationAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'university', 'duration')

admin.site.register(Education, EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company_name', 'start_date', 'end_date', 'mode_of_work', 'work_location')
    search_fields = ('position', 'company_name')

admin.site.register(Experience, ExperienceAdmin)

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress')
    search_fields = ('name',)

@admin.register(NonTechnicalSkill)
class NonTechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress')
    search_fields = ('name',)
