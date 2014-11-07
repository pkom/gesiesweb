# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0008_auto_20141107_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='miniatura',
        ),
    ]
