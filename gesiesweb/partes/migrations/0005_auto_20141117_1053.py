# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0004_auto_20141114_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parteseguimiento',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='parte',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2014, 11, 17, 9, 53, 8, 655410, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parteseguimiento',
            name='parte',
            field=models.ForeignKey(related_name='seguimientos', to='partes.Parte'),
            preserve_default=True,
        ),
    ]
