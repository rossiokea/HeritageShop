# Generated by Django 4.1.2 on 2022-11-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_vehicle_vehicle_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_identifier',
            field=models.IntegerField(),
        ),
    ]
