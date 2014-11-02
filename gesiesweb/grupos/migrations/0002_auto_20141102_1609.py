# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
        ('profesores', '0002_auto_20141102_1609'),
        ('alumnos', '0002_cursoalumno'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoprofesor',
            name='profesor',
            field=models.ForeignKey(to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grupoalumno',
            name='alumno',
            field=models.ForeignKey(to='alumnos.CursoAlumno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grupoalumno',
            name='grupo',
            field=models.ForeignKey(to='grupos.CursoGrupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursogrupo',
            name='curso',
            field=models.ForeignKey(to='cursos.Curso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursogrupo',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursogrupo',
            name='tutor',
            field=models.ForeignKey(to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
    ]
