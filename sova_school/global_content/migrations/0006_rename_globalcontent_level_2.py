# Generated by Django 5.0a1 on 2023-10-08 14:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("global_content", "0005_remove_globalcontent_photos_globalcontent_file"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="GlobalContent",
            new_name="Level_2",
        ),
    ]
