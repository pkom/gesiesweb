# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignaturas', '0002_auto_20141102_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignatura',
            options={'ordering': ['abreviatura']},
        ),
        migrations.AlterModelOptions(
            name='departamentoasignatura',
            options={'ordering': ['asignatura__abreviatura']},
        ),
    ]
