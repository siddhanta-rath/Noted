# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_tag_usertag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='usertag',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UserTag',
        ),
    ]