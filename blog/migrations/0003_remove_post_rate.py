# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rate',
        ),
    ]
