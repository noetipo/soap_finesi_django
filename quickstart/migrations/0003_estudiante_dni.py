# Generated by Django 2.1.7 on 2019-02-15 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_pagos_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='dni',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
