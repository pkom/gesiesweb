# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0003_auto_20150506_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursogrupo',
            name='curso',
            field=models.ForeignKey(related_name='cursogrupos', to='cursos.Curso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursogrupo',
            name='grupo',
            field=models.ForeignKey(related_name='grupos', to='grupos.Grupo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursogrupo',
            name='tutor',
            field=models.ForeignKey(related_name='tutores', blank=True, to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grupoalumno',
            name='cursoalumno',
            field=models.ForeignKey(related_name='alumnos', to='alumnos.CursoAlumno'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grupoalumno',
            name='cursogrupo',
            field=models.ForeignKey(related_name='grupoalumnos', to='grupos.CursoGrupo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grupoprofesor',
            name='cursogrupo',
            field=models.ForeignKey(related_name='grupoprofesores', to='grupos.CursoGrupo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grupoprofesor',
            name='cursoprofesor',
            field=models.ForeignKey(related_name='profesores', to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
    ]
