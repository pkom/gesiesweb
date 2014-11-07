# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_auto_20141102_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellidos',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
