# Generated by Django 4.2.3 on 2023-07-23 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("A2Zbackend", "0006_remove_dispatchentry_partner_caseid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dispatchentry",
            name="repair_status",
        ),
    ]
