# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0009_auto_20141105_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departamentoprofesor',
            old_name='profesor',
            new_name='cursoprofesor',
        ),
        migrations.AlterUniqueTogether(
            name='departamentoprofesor',
            unique_together=set([('cursodepartamento', 'cursoprofesor')]),
        ),
    ]
