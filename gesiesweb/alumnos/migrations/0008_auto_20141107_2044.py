# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_auto_20141107_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(default=b'', upload_to=b'alumnos/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='miniatura',
            field=models.ImageField(default=b'', upload_to=b'miniaturas/', editable=False, blank=True),
            preserve_default=True,
        ),
    ]
