# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0005_auto_20141102_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='departamento',
            field=models.CharField(max_length=50, db_index=True),
            preserve_default=True,
        ),
    ]
