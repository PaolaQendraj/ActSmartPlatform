# Generated by Django 3.0.8 on 2020-07-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_header',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
