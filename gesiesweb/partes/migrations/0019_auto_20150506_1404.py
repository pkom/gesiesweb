# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0018_auto_20150506_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 6, 12, 4, 25, 996066, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
