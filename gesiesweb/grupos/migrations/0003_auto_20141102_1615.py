# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_auto_20141102_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='descripcion',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
