# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0006_auto_20141102_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cursogrupo',
            unique_together=set([('curso', 'grupo')]),
        ),
        migrations.AlterUniqueTogether(
            name='grupoalumno',
            unique_together=set([('grupo', 'alumno')]),
        ),
        migrations.AlterUniqueTogether(
            name='grupoprofesor',
            unique_together=set([('grupo', 'profesor')]),
        ),
    ]
