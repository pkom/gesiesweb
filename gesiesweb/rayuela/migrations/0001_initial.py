# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rayuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('tipo', models.CharField(max_length=2, choices=[(b'PR', b'Profesores'), (b'AL', b'Alumnos')])),
                ('archivo', models.FileField(upload_to=b'rayuela/%Y/%m/%d')),
                ('procesado', models.BooleanField(default=False)),
                ('resultado', models.TextField(null=True, blank=True)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
