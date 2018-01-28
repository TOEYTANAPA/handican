# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20180126_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='qulification',
            new_name='qualification',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_image',
        ),
        migrations.RemoveField(
            model_name='job',
            name='traveling',
        ),
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.CharField(default='ไม่ระบุ', max_length=5000),
        ),
    ]
