# Generated by Django 4.2.2 on 2023-08-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0003_content_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="user_choices",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Yes", "Yes"),
                    ("No", "No"),
                    ("I am not sure", "I Am Not Sure"),
                    ("Choice answer:", "Choice Answer"),
                ],
                default="Choice answer:",
                max_length=20,
            ),
        ),
    ]
