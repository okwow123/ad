# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_type',
            field=models.BooleanField(default=True),
        ),
    ]
