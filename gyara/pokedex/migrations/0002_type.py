# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
                ('pokemon', models.ManyToManyField(to='pokedex.Pokemon')),
                ('strengths', models.ManyToManyField(related_name='_type_strengths_+', to='pokedex.Type')),
                ('weaknesses', models.ManyToManyField(related_name='_type_weaknesses_+', to='pokedex.Type')),
            ],
        ),
    ]
