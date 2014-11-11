# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '__first__'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoDepartamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
            ],
            options={
                'ordering': ['curso__curso', 'departamento__departamento'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('departamento', models.CharField(unique=True, max_length=100, db_index=True)),
                ('descripcion', models.TextField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['departamento'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepartamentoProfesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('cursodepartamento', models.ForeignKey(to='departamentos.CursoDepartamento')),
                ('cursoprofesor', models.ForeignKey(to='profesores.CursoProfesor')),
            ],
            options={
                'ordering': ['cursodepartamento__curso__curso', 'cursodepartamento__departamento__departamento', 'cursoprofesor__profesor__user__last_name', 'cursoprofesor__profesor__user__first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='departamentoprofesor',
            unique_together=set([('cursodepartamento', 'cursoprofesor')]),
        ),
        migrations.AddField(
            model_name='cursodepartamento',
            name='departamento',
            field=models.ForeignKey(to='departamentos.Departamento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cursodepartamento',
            name='jefe',
            field=models.ForeignKey(blank=True, to='profesores.CursoProfesor', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cursodepartamento',
            unique_together=set([('curso', 'departamento')]),
        ),
    ]
