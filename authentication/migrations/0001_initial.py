# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-03 09:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, default='')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('role', models.CharField(choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')], default='mentee', max_length=6)),
                ('phone_number', models.CharField(blank=True, max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_profile',
            },
        ),
        migrations.AddField(
            model_name='interest',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='interest',
            unique_together=set([('interest', 'profile')]),
        ),
        migrations.AlterIndexTogether(
            name='interest',
            index_together=set([('interest', 'profile')]),
        ),
    ]
