# Generated by Django 3.1.6 on 2021-02-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0007_auto_20210203_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='location',
            field=models.ManyToManyField(to='doctorapi.Location'),
        ),
    ]
