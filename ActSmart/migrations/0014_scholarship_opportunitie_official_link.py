# Generated by Django 3.0.8 on 2020-07-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0013_program_opportunitie_official_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship_opportunitie',
            name='official_link',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
