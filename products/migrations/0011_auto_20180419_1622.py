# Generated by Django 2.0.3 on 2018-04-19 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20180419_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='product_name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='product_rating',
            new_name='item_rating',
        ),
    ]
