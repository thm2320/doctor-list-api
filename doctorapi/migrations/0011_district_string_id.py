# Generated by Django 3.1.6 on 2021-02-04 07:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0010_operationschedule_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='string_id',
            field=models.CharField(default=uuid.uuid4, max_length=60, null=True),
        ),
    ]
