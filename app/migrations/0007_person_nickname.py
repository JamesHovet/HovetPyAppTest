# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_person_ismale'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nickname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]