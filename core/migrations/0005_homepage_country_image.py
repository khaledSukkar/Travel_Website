# Generated by Django 5.0.6 on 2024-06-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_reservation_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_page/images/')),
                ('title', models.CharField(max_length=300)),
                ('sub_title', models.CharField(max_length=600)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(null=True, upload_to='countries/images/'),
        ),
    ]
