# Generated by Django 4.2.4 on 2023-08-31 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GlobalContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("image_url", models.URLField(blank=True, null=True)),
                (
                    "photos",
                    models.ImageField(blank=True, null=True, upload_to="photos"),
                ),
            ],
        ),
    ]
