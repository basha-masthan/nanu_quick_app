# Generated by Django 5.0.6 on 2024-08-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickapp', '0019_remove_doctor_data_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_data',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
