# Generated by Django 4.1.2 on 2022-11-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_equipment_equipment_identifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_description',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_short_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
