# Generated by Django 5.0.4 on 2024-04-22 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiflow', '0006_sistema_tipo_soporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='sistema_padre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atiflow.sistema'),
        ),
    ]
