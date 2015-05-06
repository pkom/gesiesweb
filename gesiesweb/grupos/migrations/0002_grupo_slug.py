# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='slug',
            field=models.SlugField(default=b'aas', max_length=10),
            preserve_default=True,
        ),
    ]
