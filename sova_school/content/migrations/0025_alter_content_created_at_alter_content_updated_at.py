# Generated by Django 4.2.2 on 2023-07-27 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0024_alter_content_created_at_alter_content_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 27, 12, 59, 34, 337345)
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 27, 12, 59, 34, 337345)
            ),
        ),
    ]
