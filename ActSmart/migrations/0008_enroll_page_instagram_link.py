# Generated by Django 3.0.8 on 2020-07-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActSmart', '0007_enroll_content_list_enroll_page_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='enroll_page',
            name='instagram_link',
            field=models.CharField(default='', max_length=50),
        ),
    ]