# Generated by Django 4.1.2 on 2023-07-04 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0002_remove_product_category_ad_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_ad.category'),
        ),
    ]
