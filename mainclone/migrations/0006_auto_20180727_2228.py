# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainclone', '0005_auto_20180724_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photolikes', to='mainclone.Post'),
        ),
    ]
