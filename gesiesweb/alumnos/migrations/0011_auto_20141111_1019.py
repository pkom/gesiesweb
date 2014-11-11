# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0010_auto_20141107_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'ordering': ['apellidos', 'nombre']},
        ),
        migrations.AlterModelOptions(
            name='cursoalumno',
            options={'ordering': ['alumno__apellidos', 'alumno__nombre']},
        ),
    ]
