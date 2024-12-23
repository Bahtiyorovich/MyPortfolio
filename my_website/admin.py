from django.contrib import admin
from django.utils.html import format_html

from my_website.models import (
    CustomUser, AboutMe,
    Experience, Project,
    Education, YoutubeVideo,
    Skill, ProjectImage,
    )

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff',)


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('my_name', 'user',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('university', 'degree', 'start_year', 'end_year',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_year', 'end_year')


@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title','link')
    search_fields = ('title', 'link')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px; height:avto;" />', obj.image.url)
        return "No image"

    preview.short_description = 'Image Preview'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'project_type', 'service', 'client', 'create_date', 'is_active',  )
    inlines = [ProjectImageInline]