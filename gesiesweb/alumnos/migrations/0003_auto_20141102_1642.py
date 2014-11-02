# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_cursoalumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellidos',
            field=models.CharField(max_length=40, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nie',
            field=models.CharField(unique=True, max_length=15, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=20, db_index=True),
            preserve_default=True,
        ),
    ]
