# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_auto_20180515_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='date_of_confirmation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]