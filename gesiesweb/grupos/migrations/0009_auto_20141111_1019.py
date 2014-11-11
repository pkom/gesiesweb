# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0008_auto_20141106_1802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursogrupo',
            options={'ordering': ['curso__curso', 'grupo__grupo']},
        ),
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ['grupo']},
        ),
        migrations.AlterModelOptions(
            name='grupoalumno',
            options={'ordering': ['cursogrupo__curso__curso', 'cursogrupo__grupo__grupo', 'cursoalumno__alumno__apellidos', 'cursoalumno__alumno__nombre']},
        ),
        migrations.AlterModelOptions(
            name='grupoprofesor',
            options={'ordering': ['cursogrupo__curso__curso', 'cursogrupo__grupo__grupo', 'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name']},
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(unique=True, max_length=10, db_index=True),
            preserve_default=True,
        ),
    ]
