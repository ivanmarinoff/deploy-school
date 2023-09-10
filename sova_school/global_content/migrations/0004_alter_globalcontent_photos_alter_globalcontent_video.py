# Generated by Django 4.2.5 on 2023-09-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("global_content", "0003_globalcontent_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalcontent",
            name="photos",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="photos"
            ),
        ),
        migrations.AlterField(
            model_name="globalcontent",
            name="video",
            field=models.FileField(
                blank=True, default=None, null=True, upload_to="videos"
            ),
        ),
    ]