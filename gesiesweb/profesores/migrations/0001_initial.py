# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import model_utils.fields
import profesores.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoProfesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
            ],
            options={
                'ordering': ['curso__curso', 'profesor__user__last_name', 'profesor__user__first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('dni', models.CharField(default=b'', unique=True, max_length=20, db_index=True, blank=True)),
                ('usuario_rayuela', models.CharField(default=b'', max_length=20, blank=True)),
                ('foto', sorl.thumbnail.fields.ImageField(default=b'', upload_to=profesores.models.upload_to, blank=True)),
                ('es_usuario', models.BooleanField(default=False)),
                ('id_usuario', models.CharField(default=b'', max_length=20, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__last_name', 'user__first_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cursoprofesor',
            name='profesor',
            field=models.ForeignKey(to='profesores.Profesor'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='cursoprofesor',
            unique_together=set([('curso', 'profesor')]),
        ),
    ]
