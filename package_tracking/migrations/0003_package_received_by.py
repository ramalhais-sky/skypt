# Generated by Django 3.0.2 on 2020-01-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_tracking', '0002_auto_20200108_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='received_by',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
