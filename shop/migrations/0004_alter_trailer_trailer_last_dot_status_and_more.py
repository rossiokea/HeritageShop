# Generated by Django 4.1.2 on 2022-11-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_trailer_trailer_last_dot_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='trailer_last_dot_status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trailerdotrecord',
            name='trailer_dot_passed_inspection',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
