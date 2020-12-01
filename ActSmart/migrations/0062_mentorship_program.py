# Generated by Django 3.0.8 on 2020-09-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0061_auto_20200912_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorship_Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, null=True)),
                ('features', models.TextField(default='')),
            ],
        ),
    ]