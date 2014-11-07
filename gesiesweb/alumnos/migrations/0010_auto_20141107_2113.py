# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_remove_alumno_miniatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default=b'', upload_to=b'alumnos', blank=True),
            preserve_default=True,
        ),
    ]
