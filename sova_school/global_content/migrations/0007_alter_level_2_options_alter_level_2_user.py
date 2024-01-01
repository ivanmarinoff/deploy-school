# Generated by Django 4.2.6 on 2023-10-22 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("global_content", "0006_rename_globalcontent_level_2"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="level_2",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="level_2",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
