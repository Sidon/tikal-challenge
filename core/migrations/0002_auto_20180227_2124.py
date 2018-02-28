# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-27 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='dados_processo',
            field=models.TextField(verbose_name='Dados'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='numero_processo',
            field=models.CharField(max_length=20, unique=True, verbose_name='Número'),
        ),
    ]