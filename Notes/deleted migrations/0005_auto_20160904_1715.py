# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 11:45
from __future__ import unicode_literals

import Notes.current_user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notes', '0004_auto_20160728_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='listdos',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='notes',
        ),
        migrations.AddField(
            model_name='usertag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.Tag'),
        ),
        migrations.AddField(
            model_name='usertag',
            name='user',
            field=models.ForeignKey(default=Notes.current_user.get_current_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]