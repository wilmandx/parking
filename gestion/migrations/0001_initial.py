# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('horas', models.IntegerField(default=0)),
                ('dias', models.IntegerField(default=0)),
                ('valor', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValorTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(max_length=3000)),
                ('activo', models.BooleanField(default=True)),
                ('padre', models.ForeignKey(to='gestion.ValorTipo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tarifa',
            name='tipoTarifa',
            field=models.ForeignKey(to='gestion.ValorTipo'),
            preserve_default=True,
        ),
    ]
