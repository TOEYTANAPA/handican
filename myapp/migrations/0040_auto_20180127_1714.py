# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-27 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20180127_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='detail',
            field=models.CharField(default='ไม่ระบุ', max_length=5000),
        ),
    ]
