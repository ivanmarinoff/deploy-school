# Generated by Django 5.0 on 2024-01-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Level_1",
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
                    "file",
                    models.FileField(
                        blank=True, default=None, null=True, upload_to="files"
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True, default=None, null=True, upload_to="videos"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
