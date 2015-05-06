# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_departamento_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='slug',
            field=models.SlugField(max_length=100),
            preserve_default=True,
        ),
    ]
