# Generated by Django 3.0.8 on 2020-09-10 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0044_auto_20200910_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
