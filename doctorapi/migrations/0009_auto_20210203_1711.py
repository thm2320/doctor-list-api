# Generated by Django 3.1.6 on 2021-02-03 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0008_doctor_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='location',
            new_name='locations',
        ),
    ]
