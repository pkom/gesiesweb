# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_cursoprofesor_es_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursoprofesor',
            name='curso',
            field=models.ForeignKey(related_name='cursos', to='cursos.Curso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cursoprofesor',
            name='profesor',
            field=models.ForeignKey(related_name='profesores', to='profesores.Profesor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='user',
            field=models.OneToOneField(related_name='profesor', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
