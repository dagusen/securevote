# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='description',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='title',
        ),
    ]