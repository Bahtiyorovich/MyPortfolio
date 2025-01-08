from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class CustomUser(AbstractUser):
    """Custom User model"""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


class AboutMe(models.Model):
    """About me model"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='about_me')
    description = HTMLField(null=True, blank=True, help_text='Write something about me')
    image = models.ImageField(null=True, blank=True, upload_to='about_me/image')
    skills = models.ManyToManyField('Skill', blank=True, help_text='Add your skills')
    my_name = models.CharField(max_length=30, help_text='Enter your name')
    social_media = models.JSONField(null=True, blank=True, help_text='Add your social media links')

    def clean(self):
        if self.social_media:
            for platform, link in self.social_media.items():
                if not link.startswith("http"):
                    raise ValidationError(f"{platform} uchun link noto'g'ri ko'rinmoqda.")

    def __str__(self):
        return self.my_name

class Education(models.Model):
    """Education model"""
    about_me = models.ForeignKey('AboutMe', on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text='Enter start year')
    end_year = models.CharField(max_length=4, help_text='Enter end year')
    degree = models.CharField(max_length=100, help_text='Enter degree')
    university = models.CharField(max_length=100, help_text='Enter university')
    description = HTMLField(help_text='Enter description')

    def __str__(self):
        return f"{self.degree} at {self.university} ({self.start_year}-{self.end_year})"


class Experience(models.Model):
    """Experience model"""
    about_me = models.ForeignKey('AboutMe', on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text='Enter start year')
    end_year = models.CharField(max_length=4, help_text='Enter end year')
    position = models.CharField(max_length=100, help_text='Enter position')
    company = models.CharField(max_length=100, help_text='Enter company')
    description = HTMLField(help_text='Enter description')

    def __str__(self):
        return f"{self.company} at {self.position} ({self.start_year}-{self.end_year})"


class Skill(models.Model):
    """Skill model"""
    name = models.CharField(max_length=100,unique=True, help_text='Enter your skill name')

    def __str__(self):
        return self.name



class Project(models.Model):
    """Project model"""
    title = models.CharField(max_length=100,unique=True, help_text='Enter your project title')
    slug = models.SlugField(unique=True, help_text='Enter your project slug', blank=True)
    description = HTMLField(help_text='Enter description')
    create_date = models.CharField(max_length=4 ,help_text='Enter start date')
    service = models.CharField(max_length=100, help_text='Enter service')
    client = models.CharField(max_length=100, help_text='Enter client')
    project_type = models.CharField(max_length=100, help_text='Enter project type')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    """Project image model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(null=True, blank=True, upload_to='project/image')

    def __str__(self):
        return f"{self.project.title}"

def validate_youtube_link(value):
    if "youtube.com" not in value and "youtu.be" not in value:
        raise ValidationError("Faqat YouTube linklarini kiriting.")

class YoutubeVideo(models.Model):
    """Youtube video model"""
    title = models.CharField(max_length=100, help_text='Enter your video title')
    link = models.URLField(validators=[validate_youtube_link], help_text='Enter Youtube video link')
    thumbnail = models.ImageField(upload_to='image/youtube_thumbnail', help_text='Enter Youtube video thumbnail')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title























