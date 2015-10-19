# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0021_auto_20150506_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='cursoprofesor',
            field=models.ForeignKey(related_name='partes', to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parte',
            name='grupoalumno',
            field=models.ForeignKey(related_name='partes', to='grupos.GrupoAlumno'),
            preserve_default=True,
        ),
    ]
