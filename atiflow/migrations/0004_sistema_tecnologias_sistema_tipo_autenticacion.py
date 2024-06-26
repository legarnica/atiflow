# Generated by Django 5.0.4 on 2024-04-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiflow', '0003_tecnologia'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='tecnologias',
            field=models.ManyToManyField(to='atiflow.tecnologia'),
        ),
        migrations.AddField(
            model_name='sistema',
            name='tipo_autenticacion',
            field=models.CharField(choices=[('SA', 'Sin Autenticación'), ('PR', 'Propia'), ('UC', 'Portal Ucampus'), ('OT', 'Otra')], default='SA', max_length=2),
        ),
    ]
