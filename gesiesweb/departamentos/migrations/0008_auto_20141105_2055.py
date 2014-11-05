# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0007_auto_20141102_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='departamento',
            field=models.CharField(max_length=100, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.TextField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
