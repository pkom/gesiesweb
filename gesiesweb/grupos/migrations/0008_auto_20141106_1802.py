# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0007_auto_20141102_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupoalumno',
            old_name='alumno',
            new_name='cursoalumno',
        ),
        migrations.RenameField(
            model_name='grupoalumno',
            old_name='grupo',
            new_name='cursogrupo',
        ),
        migrations.RenameField(
            model_name='grupoprofesor',
            old_name='grupo',
            new_name='cursogrupo',
        ),
        migrations.RenameField(
            model_name='grupoprofesor',
            old_name='profesor',
            new_name='cursoprofesor',
        ),
        migrations.AlterUniqueTogether(
            name='grupoalumno',
            unique_together=set([('cursogrupo', 'cursoalumno')]),
        ),
        migrations.AlterUniqueTogether(
            name='grupoprofesor',
            unique_together=set([('cursogrupo', 'cursoprofesor')]),
        ),
    ]
