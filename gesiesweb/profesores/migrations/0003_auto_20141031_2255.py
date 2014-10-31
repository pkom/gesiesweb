# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profesores.models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_auto_20141031_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(default=b'', upload_to=profesores.models.upload_to, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='usuario_rayuela',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
