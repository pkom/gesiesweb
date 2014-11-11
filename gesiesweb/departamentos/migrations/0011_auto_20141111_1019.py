# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0010_auto_20141105_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursodepartamento',
            options={'ordering': ['curso__curso', 'departamento__departamento']},
        ),
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['departamento']},
        ),
        migrations.AlterModelOptions(
            name='departamentoprofesor',
            options={'ordering': ['cursodepartamento__curso__curso', 'cursodepartamento__departamento__departamento', 'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name']},
        ),
        migrations.AlterField(
            model_name='departamento',
            name='departamento',
            field=models.CharField(unique=True, max_length=100, db_index=True),
            preserve_default=True,
        ),
    ]
