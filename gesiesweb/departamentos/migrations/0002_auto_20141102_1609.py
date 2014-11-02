# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        ('profesores', '0002_auto_20141102_1609'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamentoprofesor',
            name='profesor',
            field=models.ForeignKey(to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursodepartamento',
            name='curso',
            field=models.ForeignKey(to='cursos.Curso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursodepartamento',
            name='departamento',
            field=models.ForeignKey(to='departamentos.Departamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursodepartamento',
            name='jefe',
            field=models.ForeignKey(to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
    ]
