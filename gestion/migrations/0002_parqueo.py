# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parqueo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('placa', models.CharField(max_length=20)),
                ('horaEntrada', models.DateTimeField(auto_now=True)),
                ('horaSalida', models.DateTimeField()),
                ('nroFactura', models.IntegerField()),
                ('nroRecibo', models.IntegerField()),
                ('horas', models.IntegerField()),
                ('valor', models.FloatField()),
                ('tipoTarifa', models.ForeignKey(related_name='+', to='gestion.ValorTipo')),
                ('tipoVehiculo', models.ForeignKey(related_name='+', to='gestion.ValorTipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
