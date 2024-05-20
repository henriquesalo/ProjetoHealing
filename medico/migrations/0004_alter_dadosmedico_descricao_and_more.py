# Generated by Django 5.0.4 on 2024-05-17 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_datasabertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosmedico',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dadosmedico',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidades'),
        ),
    ]