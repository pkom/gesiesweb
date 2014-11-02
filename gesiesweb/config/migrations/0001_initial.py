# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('codigo_centro', models.CharField(unique=True, max_length=15)),
                ('nombre_centro', models.CharField(unique=True, max_length=50)),
                ('url_centro', models.URLField(blank=True)),
                ('email_centro', models.EmailField(max_length=254, blank=True)),
                ('direccion_centro', models.CharField(max_length=200, blank=True)),
                ('telefono_centro', models.CharField(max_length=200, blank=True)),
                ('fax_centro', models.CharField(max_length=200, blank=True)),
                ('nombre_director', models.CharField(max_length=50, blank=True)),
                ('firma_director', models.ImageField(upload_to=b'config', blank=True)),
                ('logo_centro', models.ImageField(upload_to=b'config', blank=True)),
                ('sello_centro', models.ImageField(upload_to=b'config', blank=True)),
                ('curso_academico_defecto', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cursos.Curso', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
