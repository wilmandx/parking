# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_parqueo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueo',
            name='horaSalida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
