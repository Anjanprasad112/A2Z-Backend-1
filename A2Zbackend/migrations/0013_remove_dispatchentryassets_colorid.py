# Generated by Django 4.2.3 on 2023-07-23 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("A2Zbackend", "0012_remove_dispatchentry_ata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dispatchentryassets",
            name="colorid",
        ),
    ]
