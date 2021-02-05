# Generated by Django 3.1.6 on 2021-02-05 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0013_auto_20210204_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='categories',
        ),
        migrations.AddField(
            model_name='service',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctorapi.category'),
        ),
    ]