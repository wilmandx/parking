# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_remove_tarifa_tipotarifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valortipo',
            name='nombre',
            field=models.CharField(max_length=500),
        ),
    ]
