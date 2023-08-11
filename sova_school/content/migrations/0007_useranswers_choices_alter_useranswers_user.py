# Generated by Django 4.2.2 on 2023-08-09 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0006_alter_useranswers_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="useranswers",
            name="choices",
            field=models.ManyToManyField(related_name="choices", to="content.content"),
        ),
        migrations.AlterField(
            model_name="useranswers",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]