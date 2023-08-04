# Generated by Django 4.2.2 on 2023-08-01 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0016_alter_webcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 8, 1, 15, 39, 15, 958232)
            ),
        ),
        migrations.AlterField(
            model_name="webcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 8, 1, 15, 39, 15, 958232)
            ),
        ),
    ]