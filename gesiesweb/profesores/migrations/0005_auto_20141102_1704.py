# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0004_auto_20141102_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'profesores'},
        ),
    ]
