# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_app', '0008_auto_20190619_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='show',
            name='updated_at',
        ),
    ]
