# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CattleAndPoultry',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Назва показника')),
                ('cattle', models.PositiveIntegerField()),
                ('pigs', models.PositiveIntegerField()),
                ('sheep_goat', models.PositiveIntegerField()),
                ('horses', models.PositiveIntegerField()),
                ('poultr', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LivestockProduction',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Назва показника')),
                ('unit', models.CharField(max_length=45, verbose_name='Одиниця виміру')),
                ('amount', models.PositiveIntegerField(verbose_name='Кількість')),
            ],
        ),
        migrations.CreateModel(
            name='Poultry',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Назва показника')),
                ('adult', models.PositiveIntegerField(verbose_name='Доросла')),
                ('young', models.PositiveIntegerField(verbose_name='Молодняк')),
                ('cattle_and_poultry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.CattleAndPoultry')),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name='Найменування')),
                ('business_adress_id', models.PositiveIntegerField(verbose_name='Місцезнаходження ')),
                ('actual_adress_id', models.PositiveIntegerField(verbose_name='Адреса здійснення діяльності')),
            ],
        ),
        migrations.AddField(
            model_name='livestockproduction',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.Respondent'),
        ),
        migrations.AddField(
            model_name='cattleandpoultry',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livestock.Respondent'),
        ),
    ]
