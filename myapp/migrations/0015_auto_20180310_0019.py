# Generated by Django 2.0.1 on 2018-03-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20180307_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabilityinfo',
            name='citizen_id',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='disabilityinfo',
            name='disable_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
