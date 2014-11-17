# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0005_auto_20141117_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parteseguimiento',
            old_name='profesor',
            new_name='cursoprofesor',
        ),
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 17, 11, 2, 26, 508646, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
