# Generated by Django 5.1.1 on 2024-10-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
