# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0005_auto_20141102_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(max_length=10, db_index=True),
            preserve_default=True,
        ),
    ]
