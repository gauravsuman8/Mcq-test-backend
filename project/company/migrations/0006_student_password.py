# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-28 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]