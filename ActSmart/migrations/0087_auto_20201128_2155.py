# Generated by Django 3.0.8 on 2020-11-28 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0086_opportunity_category_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity_category_region',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ActSmart.Opportunitie'),
        ),
    ]
