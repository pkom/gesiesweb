# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0003_parte_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 14, 13, 22, 7, 905392, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
