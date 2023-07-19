# Generated by Django 4.1.2 on 2023-07-04 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0005_remove_ad_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='site_ad.category'),
            preserve_default=False,
        ),
    ]