# Generated by Django 3.0.8 on 2020-09-13 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0069_auto_20200913_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='training_enroll',
            name='training',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ActSmart.Training'),
        ),
    ]