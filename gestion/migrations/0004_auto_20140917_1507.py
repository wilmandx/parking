# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20140917_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifa',
            name='tipoTarifa',
            field=models.ForeignKey(default=1, to='gestion.ValorTipo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='valortipo',
            name='padre',
            field=models.ForeignKey(blank=True, to='gestion.ValorTipo', null=True),
        ),
    ]
