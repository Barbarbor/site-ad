# Generated by Django 4.1.2 on 2023-07-16 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0016_alter_ad_seller_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]