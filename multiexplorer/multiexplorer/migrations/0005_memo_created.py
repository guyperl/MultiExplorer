# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 05:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiexplorer', '0004_auto_20170208_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
