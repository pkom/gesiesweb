# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
        ('partes', '0006_auto_20141117_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parte',
            name='cursoalumno',
        ),
        migrations.AddField(
            model_name='parte',
            name='grupoalumno',
            field=models.ForeignKey(default=1, to='grupos.GrupoAlumno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 17, 20, 32, 12, 778320, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
