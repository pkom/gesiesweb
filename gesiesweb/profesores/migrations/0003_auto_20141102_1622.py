# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_auto_20141102_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='id_usuario',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
