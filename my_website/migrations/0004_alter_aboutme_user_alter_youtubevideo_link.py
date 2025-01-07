# Generated by Django 5.1.4 on 2025-01-04 07:22

import django.db.models.deletion
import my_website.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0003_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about_me', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='link',
            field=models.URLField(help_text='Enter Youtube video link', validators=[my_website.models.validate_youtube_link]),
        ),
    ]
