# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0008_auto_20141118_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 18, 8, 51, 47, 858124, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
