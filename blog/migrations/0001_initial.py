# Generated by Django 5.1.4 on 2025-01-04 07:22

import blog.models
import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category name, e.g. , Technology', max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            bases=(blog.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Tag name, e.g. , Django', max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
            bases=(blog.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Title of the blog post...', max_length=200)),
                ('content', tinymce.models.HTMLField(help_text='Content of the blog post...')),
                ('image', models.ImageField(help_text='Upload your blog post image...', upload_to='blog/image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('comment_count', models.PositiveIntegerField(default=0, editable=False, help_text='Number of comments')),
                ('share_count', models.PositiveIntegerField(default=0, editable=False, help_text='Nubmer of shares')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('disabled', 'Disabled')], default='draft', help_text='Status of the blog post', max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, related_name='blogs', to='blog.category')),
                ('tag', models.ManyToManyField(blank=True, related_name='blogs', to='blog.tag')),
            ],
            bases=(blog.models.SlugifyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the comment', max_length=100)),
                ('email', models.EmailField(help_text='Email of the comment', max_length=254)),
                ('message', tinymce.models.HTMLField(help_text='Message of the comment')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
        ),
    ]
