# Generated by Django 3.1.6 on 2021-02-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0004_auto_20210203_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='category',
            new_name='categories',
        ),
    ]
