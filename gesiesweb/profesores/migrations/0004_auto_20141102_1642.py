# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0003_auto_20141102_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(default=b'', max_length=20, db_index=True, blank=True),
            preserve_default=True,
        ),
    ]
