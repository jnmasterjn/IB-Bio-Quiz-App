# Generated by Django 4.2.8 on 2024-12-23 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0002_alter_gamestats_score"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz_e",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=300)),
                ("answer", models.CharField(max_length=300)),
                ("optionOne", models.CharField(max_length=300)),
                ("optionTwo", models.CharField(max_length=300)),
                ("optionThree", models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name="gamestats",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
