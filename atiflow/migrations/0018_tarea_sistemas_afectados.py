# Generated by Django 5.0.4 on 2024-04-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiflow', '0017_alter_tarea_estado_delete_estadotarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='sistemas_afectados',
            field=models.ManyToManyField(blank=True, to='atiflow.sistema'),
        ),
    ]