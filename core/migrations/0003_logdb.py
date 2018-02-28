# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-27 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180227_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processo', to='core.Processo', verbose_name='Processo')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]