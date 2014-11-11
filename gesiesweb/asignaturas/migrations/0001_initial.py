# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('abreviatura', models.CharField(max_length=20, db_index=True)),
                ('asignatura', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['abreviatura'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepartamentoAsignatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('asignatura', models.ForeignKey(to='asignaturas.Asignatura')),
                ('departamento', models.ForeignKey(to='departamentos.Departamento')),
            ],
            options={
                'ordering': ['asignatura__abreviatura'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='departamentoasignatura',
            unique_together=set([('departamento', 'asignatura')]),
        ),
    ]
