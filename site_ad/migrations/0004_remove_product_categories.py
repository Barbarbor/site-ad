# Generated by Django 4.1.2 on 2023-07-04 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0003_alter_ad_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
    ]
