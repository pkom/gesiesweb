# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('parte', models.TextField()),
                ('con_parte', models.BooleanField(default=False)),
                ('comunicado', models.BooleanField(default=False)),
                ('cerrado', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(to='alumnos.CursoAlumno')),
                ('profesor', models.ForeignKey(to='profesores.CursoProfesor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParteSeguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('seguimiento', models.TextField()),
                ('parte', models.ForeignKey(to='partes.Parte')),
                ('profesor', models.ForeignKey(to='profesores.CursoProfesor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
