# Generated by Django 3.0.8 on 2020-07-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0004_auto_20200709_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='copyright_text',
            field=models.CharField(max_length=50),
        ),
    ]
