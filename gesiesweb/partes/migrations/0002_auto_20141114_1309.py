# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parte',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='parte',
            old_name='alumno',
            new_name='cursoalumno',
        ),
        migrations.RenameField(
            model_name='parte',
            old_name='profesor',
            new_name='cursoprofesor',
        ),
    ]
