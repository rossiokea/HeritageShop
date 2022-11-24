# Generated by Django 4.1.2 on 2022-11-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_equipment_equipment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailerdotrecord',
            name='trailer_dot_passed_inspection',
            field=models.BooleanField(choices=[(True, 'Passed'), (False, 'Failed')], default=True),
        ),
        migrations.AlterField(
            model_name='vehicledotrecord',
            name='dot_passed_inspection',
            field=models.BooleanField(choices=[(True, 'Passed'), (False, 'Failed')], default=True),
        ),
    ]
