# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0012_auto_20141111_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='departamento',
            field=models.CharField(unique=True, max_length=100, db_index=True),
            preserve_default=True,
        ),
    ]
