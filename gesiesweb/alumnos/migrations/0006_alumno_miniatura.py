# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_auto_20141107_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='miniatura',
            field=models.ImageField(upload_to=b'miniaturas', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
