# Generated by Django 5.0.4 on 2024-04-22 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atiflow', '0004_sistema_tecnologias_sistema_tipo_autenticacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistema',
            name='tipo_ambiente',
            field=models.CharField(choices=[('LO', 'Local'), ('TE', 'Test'), ('PR', 'Producción')], default='LO', max_length=2),
        ),
    ]