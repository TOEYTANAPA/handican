# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 16:53
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_auto_20180126_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='detail',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
