# Generated by Django 3.1.6 on 2021-02-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0002_auto_20210202_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='languages',
            field=models.ManyToManyField(to='doctorapi.Language'),
        ),
    ]
