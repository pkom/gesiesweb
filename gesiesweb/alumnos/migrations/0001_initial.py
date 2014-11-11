# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('nie', models.CharField(unique=True, max_length=15, db_index=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('usuario_rayuela', models.CharField(max_length=20, blank=True)),
                ('foto', sorl.thumbnail.fields.ImageField(default=b'', upload_to=b'alumnos', blank=True)),
            ],
            options={
                'ordering': ['apellidos', 'nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CursoAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('alumno', models.ForeignKey(to='alumnos.Alumno')),
                ('curso', models.ForeignKey(to='cursos.Curso')),
            ],
            options={
                'ordering': ['alumno__apellidos', 'alumno__nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='cursoalumno',
            unique_together=set([('curso', 'alumno')]),
        ),
        migrations.AlterIndexTogether(
            name='alumno',
            index_together=set([('apellidos', 'nombre')]),
        ),
    ]
