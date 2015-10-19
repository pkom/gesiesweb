# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoalumno',
            name='alumno',
            field=models.ForeignKey(related_name='alumnos', to='alumnos.Alumno'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursoalumno',
            name='curso',
            field=models.ForeignKey(related_name='cursoalumnos', to='cursos.Curso'),
            preserve_default=True,
        ),
    ]
