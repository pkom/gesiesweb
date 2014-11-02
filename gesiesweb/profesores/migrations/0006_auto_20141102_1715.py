# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0005_auto_20141102_1704'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cursoprofesor',
            unique_together=set([('curso', 'profesor')]),
        ),
    ]
