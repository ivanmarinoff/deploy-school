# Generated by Django 4.2.2 on 2023-08-01 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0013_alter_webcontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webcontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 8, 1, 14, 53, 30, 160442)
            ),
        ),
        migrations.AlterField(
            model_name="webcontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 8, 1, 14, 53, 30, 160442)
            ),
        ),
    ]