# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0008_auto_20141107_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursoprofesor',
            options={'ordering': ['curso__curso', 'profesor__user__last_name', 'profesor__user__first_name']},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['user__last_name', 'user__first_name']},
        ),
        migrations.AlterField(
            model_name='profesor',
            name='dni',
            field=models.CharField(default=b'', unique=True, max_length=20, db_index=True, blank=True),
            preserve_default=True,
        ),
    ]
