# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 09:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_auto_20160726_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listcontent',
            old_name='ListContent_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='listcontent',
            old_name='ListContent_checked',
            new_name='is_checked',
        ),
        migrations.RenameField(
            model_name='listdo',
            old_name='ListDo_remainder',
            new_name='listdo_remainder',
        ),
        migrations.RenameField(
            model_name='listdo',
            old_name='ListDo_title',
            new_name='listdo_title',
        ),
    ]
