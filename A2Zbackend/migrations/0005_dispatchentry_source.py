# Generated by Django 4.2.3 on 2023-07-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("A2Zbackend", "0004_remove_dispatchentryassets_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="dispatchentry",
            name="source",
            field=models.CharField(default="web", max_length=100),
        ),
    ]
