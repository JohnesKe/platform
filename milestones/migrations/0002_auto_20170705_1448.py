# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-05 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milestones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='start_date',
            field=models.DateField(),
        ),
    ]