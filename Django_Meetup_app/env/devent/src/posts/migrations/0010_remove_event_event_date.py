# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20160304_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
    ]
