# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180117_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['pubDateTime']},
        ),
        migrations.AddField(
            model_name='comment',
            name='pubDateTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
