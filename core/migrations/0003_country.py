# Generated by Django 5.0.2 on 2024-06-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_remove_doctor_pharmacyid_remove_doctor_specialty_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country_name", models.CharField(max_length=50)),
            ],
        ),
    ]
