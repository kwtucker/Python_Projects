# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160304_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]