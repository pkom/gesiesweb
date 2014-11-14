# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0002_auto_20141114_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 14, 13, 16, 24, 14266, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
