# Generated by Django 4.1.2 on 2023-07-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0009_rename_title_ad_name_remove_ad_seller_ad_added_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='photo_large',
            field=models.ImageField(blank=True, null=True, upload_to='ad_photos/large'),
        ),
        migrations.AddField(
            model_name='ad',
            name='photo_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='ad_photos/thumbnails'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ad_photos'),
        ),
    ]
