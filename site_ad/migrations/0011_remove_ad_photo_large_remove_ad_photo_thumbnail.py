# Generated by Django 4.1.2 on 2023-07-10 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0010_ad_photo_large_ad_photo_thumbnail_alter_ad_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='photo_large',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='photo_thumbnail',
        ),
    ]