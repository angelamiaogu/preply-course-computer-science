# Generated by Django 4.2.13 on 2024-06-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0002_alter_lesson_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="content",
            field=models.JSONField(),
        ),
    ]