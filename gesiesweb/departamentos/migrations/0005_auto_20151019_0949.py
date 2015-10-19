# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0004_auto_20150506_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursodepartamento',
            name='curso',
            field=models.ForeignKey(related_name='cursodepartamentos', to='cursos.Curso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursodepartamento',
            name='departamento',
            field=models.ForeignKey(related_name='departamentos', to='departamentos.Departamento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursodepartamento',
            name='jefe',
            field=models.ForeignKey(related_name='jefes', blank=True, to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamentoprofesor',
            name='cursodepartamento',
            field=models.ForeignKey(related_name='cursodepartamentos', to='departamentos.CursoDepartamento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamentoprofesor',
            name='cursoprofesor',
            field=models.ForeignKey(related_name='cursoprofesores', to='profesores.CursoProfesor'),
            preserve_default=True,
        ),
    ]
