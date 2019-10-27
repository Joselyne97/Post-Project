# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-27 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='vote',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
