# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_auto_20161017_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='cannot_affect',
            field=models.ManyToManyField(related_name='_type_cannot_affect_+', to='pokedex.Type'),
        ),
    ]