# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20151019_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='firma_director',
            field=models.ImageField(upload_to=b'config', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='config',
            name='logo_centro',
            field=models.ImageField(upload_to=b'config', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='config',
            name='sello_centro',
            field=models.ImageField(upload_to=b'config', blank=True),
            preserve_default=True,
        ),
    ]
