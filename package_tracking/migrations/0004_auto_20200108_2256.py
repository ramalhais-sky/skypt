# Generated by Django 3.0.2 on 2020-01-08 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package_tracking', '0003_package_received_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='image',
            new_name='image_text',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='received_by',
            new_name='received_by_text',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='recipient',
            new_name='recipient_text',
        ),
    ]
