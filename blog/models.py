from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class SlugifyMixin:
    slug_source_field = 'name'
    slug_target_field = 'slug'

    def save(self, *args, **kwargs):
        if not getattr(self, self.slug_target_field) and getattr(self, self.slug_source_field):
            source = getattr(self, self.slug_source_field)
            setattr(self, self.slug_target_field, slugify(source))
        super().save(*args, **kwargs)


# Create your models here.
class Category(SlugifyMixin, models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Category name, e.g. , Technology")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

class Tag(SlugifyMixin, models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Tag name, e.g. , Django")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name


class Blog(SlugifyMixin, models.Model):
    """Blog post model"""

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('disabled', 'Disabled')
    )

    name = models.CharField(max_length=200, help_text='Title of the blog post...')
    content = HTMLField(help_text="Content of the blog post...")
    image = models.ImageField(upload_to="blog/image", help_text="Upload your blog post image...")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            related_name='blog_posts',
            null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)
    tag = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    comments_count = models.PositiveIntegerField(default=0, editable=False, help_text='Number of comments')
    share_count = models.PositiveIntegerField(default=0, editable=False, help_text='Nubmer of shares')
    status = models.CharField(
              max_length=10,
              choices=STATUS_CHOICES,
              default='draft',
              help_text='Status of the blog post')

    def update_comments_count(self):
        """Update the count of comments for this blog"""
        self.comments_count = self.comments.count()
        self.save()


class Comment(models.Model):
    """Blog comment model"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, help_text='Name of the comment')
    email = models.EmailField(help_text='Email of the comment')
    message = HTMLField(help_text='Message of the comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.name}"


