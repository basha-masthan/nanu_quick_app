# Generated by Django 5.0.6 on 2024-08-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickapp', '0025_alter_user_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_appointment',
            name='pusername',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
