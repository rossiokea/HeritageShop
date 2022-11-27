# Generated by Django 4.1.2 on 2022-11-27 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_equipment_equipment_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment_department',
            field=models.IntegerField(blank=True, choices=[('', 'Select One'), (10, 'Construction'), (20, 'Maintenance'), (50, 'Admin')], null=True),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='trailer_department',
            field=models.IntegerField(blank=True, choices=[('', 'Select One'), (10, 'Construction'), (20, 'Maintenance'), (50, 'Admin')], null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_department',
            field=models.IntegerField(blank=True, choices=[('', 'Select One'), (10, 'Construction'), (20, 'Maintenance'), (50, 'Admin')], null=True),
        ),
    ]
