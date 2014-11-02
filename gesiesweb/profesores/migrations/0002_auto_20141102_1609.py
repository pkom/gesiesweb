# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoProfesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
                ('profesor', models.ForeignKey(to='profesores.Profesor')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profesor',
            name='es_usuario',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='id_usuario',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
