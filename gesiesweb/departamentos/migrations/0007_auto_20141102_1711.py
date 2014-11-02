# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0006_auto_20141102_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cursodepartamento',
            unique_together=set([('curso', 'departamento')]),
        ),
        migrations.AlterUniqueTogether(
            name='departamentoprofesor',
            unique_together=set([('departamento', 'profesor')]),
        ),
    ]
