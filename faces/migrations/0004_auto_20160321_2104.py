# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faces', '0003_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='cor_coef',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='results',
            name='p_value',
            field=models.IntegerField(max_length=50),
        ),
    ]