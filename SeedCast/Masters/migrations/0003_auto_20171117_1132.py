# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0002_auto_20171114_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Varietynew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ViewDealerlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Masters.Districts')),
            ],
        ),
        migrations.RemoveField(
            model_name='pilotplots',
            name='panchayat_name',
        ),
        migrations.AlterField(
            model_name='dealer_registration',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 17, 11, 32, 54, 346982)),
        ),
        migrations.AlterField(
            model_name='vawdemand',
            name='date_collected',
            field=models.DateField(default=datetime.datetime(2017, 11, 17, 11, 32, 54, 352135)),
        ),
    ]
