# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=2019),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]