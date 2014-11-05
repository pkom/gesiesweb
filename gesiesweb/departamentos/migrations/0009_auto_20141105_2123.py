# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0008_auto_20141105_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamentoprofesor',
            old_name='departamento',
            new_name='cursodepartamento',
        ),
        migrations.AlterUniqueTogether(
            name='departamentoprofesor',
            unique_together=set([('cursodepartamento', 'profesor')]),
        ),
    ]
