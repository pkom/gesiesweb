# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_auto_20141102_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellidos',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cursoalumno',
            unique_together=set([('curso', 'alumno')]),
        ),
        migrations.AlterIndexTogether(
            name='alumno',
            index_together=set([('apellidos', 'nombre')]),
        ),
    ]
