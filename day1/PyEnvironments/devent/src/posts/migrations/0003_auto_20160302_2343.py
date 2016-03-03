# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-02 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160302_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='meetup_id',
            field=models.IntegerField(default=0),
        ),
    ]