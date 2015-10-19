# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0003_auto_20151019_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='usuario_rayuela',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
