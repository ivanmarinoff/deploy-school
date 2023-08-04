# Generated by Django 4.2.2 on 2023-07-30 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0042_alter_useranswers_user_answers"),
    ]

    operations = [
        migrations.AddField(
            model_name="useranswers",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="useranswers",
            name="user_answers",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="content.content"
            ),
        ),
    ]