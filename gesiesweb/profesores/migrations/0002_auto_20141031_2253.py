# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profesores.models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='dni',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(null=True, upload_to=profesores.models.upload_to, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='usuario_rayuela',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
