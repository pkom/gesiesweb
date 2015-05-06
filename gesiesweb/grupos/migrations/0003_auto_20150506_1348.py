# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_grupo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='slug',
            field=models.SlugField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
