# Generated by Django 3.1.6 on 2021-02-04 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0009_auto_20210203_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=255)),
                ('times', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('priceDetails', models.TextField(null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doctorapi.doctor')),
                ('operation_schedules', models.ManyToManyField(to='doctorapi.OperationSchedule')),
            ],
        ),
    ]
