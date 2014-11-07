# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import profesores.models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0007_auto_20141105_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default=b'', upload_to=profesores.models.upload_to, blank=True),
            preserve_default=True,
        ),
    ]
