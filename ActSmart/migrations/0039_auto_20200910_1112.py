# Generated by Django 3.0.8 on 2020-09-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0038_user_profile_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='mediaa'),
        ),
    ]