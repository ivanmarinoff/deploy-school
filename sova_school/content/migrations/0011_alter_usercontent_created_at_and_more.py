# Generated by Django 4.2.2 on 2023-07-18 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0010_alter_usercontent_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercontent",
            name="created_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 18, 14, 2, 55, 341141)
            ),
        ),
        migrations.AlterField(
            model_name="usercontent",
            name="updated_at",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 7, 18, 14, 2, 55, 341141)
            ),
        ),
    ]
