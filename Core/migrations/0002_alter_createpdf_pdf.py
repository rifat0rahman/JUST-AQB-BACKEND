# Generated by Django 5.1.7 on 2025-03-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createpdf",
            name="pdf",
            field=models.CharField(default="", max_length=400),
        ),
    ]
