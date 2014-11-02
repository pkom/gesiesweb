# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_auto_20141102_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursodepartamento',
            name='jefe',
            field=models.ForeignKey(to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
    ]
