# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20140929_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueo',
            name='horas',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='parqueo',
            name='nroFactura',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='parqueo',
            name='nroRecibo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='parqueo',
            name='valor',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
