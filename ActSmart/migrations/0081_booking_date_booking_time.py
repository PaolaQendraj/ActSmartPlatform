# Generated by Django 3.0.8 on 2020-11-23 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0080_auto_20201115_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=2)),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ActSmart.Booking_Date')),
            ],
        ),
    ]