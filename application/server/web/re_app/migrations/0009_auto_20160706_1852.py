# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('re_app', '0008_auto_20160702_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='day_close',
            field=models.CharField(choices=[('\u041f\u043d', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), ('\u0412\u0442', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), ('\u0421\u0440', '\u0421\u0440\u0435\u0434\u0430'), ('\u0427\u0442', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), ('\u041f\u0442', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), ('\u0421\u0431', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), ('\u0412\u0441', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u0438\u0435')], default='\u0421\u0431', max_length=2, verbose_name='\u043f\u043e'),
        ),
        migrations.AddField(
            model_name='station',
            name='day_open',
            field=models.CharField(choices=[('\u041f\u043d', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), ('\u0412\u0442', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), ('\u0421\u0440', '\u0421\u0440\u0435\u0434\u0430'), ('\u0427\u0442', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), ('\u041f\u0442', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), ('\u0421\u0431', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), ('\u0412\u0441', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u0438\u0435')], default='\u041f\u043d', max_length=2, verbose_name='\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0441'),
        ),
    ]
