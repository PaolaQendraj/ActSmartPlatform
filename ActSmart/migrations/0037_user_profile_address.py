# Generated by Django 3.0.8 on 2020-09-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0036_auto_20200910_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
