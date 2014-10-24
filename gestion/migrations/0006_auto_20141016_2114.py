# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_constante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constante',
            name='descripcion',
            field=models.CharField(null=True, max_length=500, blank=True),
        ),
    ]
