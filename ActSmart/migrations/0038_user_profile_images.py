# Generated by Django 3.0.8 on 2020-09-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0037_user_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
