# Generated by Django 4.2.6 on 2023-10-22 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0003_level_1_delete_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="level_1",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="level_1",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]