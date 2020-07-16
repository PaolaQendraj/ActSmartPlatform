# Generated by Django 3.0.8 on 2020-07-09 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0008_enroll_page_instagram_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=170)),
                ('image', models.ImageField(upload_to='media')),
                ('deadline', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('objectives', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('founded', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
                ('eligibility', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ActSmart.Opportunitie')),
            ],
        ),
    ]
