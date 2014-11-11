# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('curso', models.CharField(unique=True, max_length=9)),
                ('retrasos_para_amonestacion', models.PositiveSmallIntegerField(default=2)),
                ('retrasos_por_trimestres', models.BooleanField(default=True)),
                ('inicio_trimestre_1', models.DateField()),
                ('fin_trimestre_1', models.DateField()),
                ('inicio_trimestre_2', models.DateField()),
                ('fin_trimestre_2', models.DateField()),
                ('inicio_trimestre_3', models.DateField()),
                ('fin_trimestre_3', models.DateField()),
                ('peso_1', models.DecimalField(default=100, max_digits=5, decimal_places=2)),
                ('peso_2', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('peso_3', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('peso_4', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('peso_5', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('peso_6', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
            ],
            options={
                'ordering': ['curso'],
            },
            bases=(models.Model,),
        ),
    ]
