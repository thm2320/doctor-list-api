# Generated by Django 3.1.6 on 2021-02-05 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0014_auto_20210205_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='categories',
            new_name='category',
        ),
    ]
