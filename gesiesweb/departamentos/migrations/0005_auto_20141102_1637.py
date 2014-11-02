# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0004_auto_20141102_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursodepartamento',
            name='jefe',
            field=models.ForeignKey(blank=True, to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
    ]
