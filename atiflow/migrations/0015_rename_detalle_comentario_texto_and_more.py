# Generated by Django 5.0.4 on 2024-04-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiflow', '0014_tarea_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='detalle',
            new_name='texto',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='fecha',
        ),
    ]
