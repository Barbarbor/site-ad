# Generated by Django 4.1.2 on 2023-07-04 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_ad', '0007_remove_ad_category_ad_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='category',
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='site_ad.category'),
            preserve_default=False,
        ),
    ]