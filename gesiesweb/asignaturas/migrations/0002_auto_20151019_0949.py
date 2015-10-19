# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignaturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentoasignatura',
            name='asignatura',
            field=models.ForeignKey(related_name='asignaturas', to='asignaturas.Asignatura'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamentoasignatura',
            name='departamento',
            field=models.ForeignKey(related_name='departamentoasignaturas', to='departamentos.Departamento'),
            preserve_default=True,
        ),
    ]
