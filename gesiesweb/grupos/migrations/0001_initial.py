# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '__first__'),
        ('cursos', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoGrupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
            ],
            options={
                'ordering': ['curso__curso', 'grupo__grupo'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('grupo', models.CharField(unique=True, max_length=10, db_index=True)),
                ('descripcion', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'ordering': ['grupo'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupoAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('cursoalumno', models.ForeignKey(to='alumnos.CursoAlumno')),
                ('cursogrupo', models.ForeignKey(to='grupos.CursoGrupo')),
            ],
            options={
                'ordering': ['cursogrupo__curso__curso', 'cursogrupo__grupo__grupo', 'cursoalumno__alumno__apellidos', 'cursoalumno__alumno__nombre'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrupoProfesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('cursogrupo', models.ForeignKey(to='grupos.CursoGrupo')),
                ('cursoprofesor', models.ForeignKey(to='profesores.CursoProfesor')),
            ],
            options={
                'ordering': ['cursogrupo__curso__curso', 'cursogrupo__grupo__grupo', 'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='grupoprofesor',
            unique_together=set([('cursogrupo', 'cursoprofesor')]),
        ),
        migrations.AlterUniqueTogether(
            name='grupoalumno',
            unique_together=set([('cursogrupo', 'cursoalumno')]),
        ),
        migrations.AddField(
            model_name='cursogrupo',
            name='grupo',
            field=models.ForeignKey(to='grupos.Grupo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursogrupo',
            name='tutor',
            field=models.ForeignKey(blank=True, to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cursogrupo',
            unique_together=set([('curso', 'grupo')]),
        ),
    ]
