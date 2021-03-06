# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainclone', '0008_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='saves',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainclone.Post'),
        ),
        migrations.AddField(
            model_name='saves',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saves', to='mainclone.Profile'),
        ),
    ]
