# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 01:49
from __future__ import unicode_literals

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_arquivquestao_arquivresposta_coordenador_cursturma_disciplina_disciplinofertada_grade_matricula_peri'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
    ]
