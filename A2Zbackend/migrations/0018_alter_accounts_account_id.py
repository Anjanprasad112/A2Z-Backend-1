# Generated by Django 4.2.3 on 2023-07-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("A2Zbackend", "0017_alter_vehicles_vehicle_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounts",
            name="account_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
