# Generated by Django 5.0.4 on 2024-06-10 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.country'),
        ),
    ]
