# Generated by Django 4.1.2 on 2023-07-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0018_ad_email_ad_location_ad_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
