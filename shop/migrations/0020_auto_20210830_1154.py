# Generated by Django 3.1.7 on 2021-08-30 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_product_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='admin_id',
        ),
    ]