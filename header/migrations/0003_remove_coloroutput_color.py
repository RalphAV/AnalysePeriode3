# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-06 11:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_coloroutput'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coloroutput',
            name='color',
        ),
    ]