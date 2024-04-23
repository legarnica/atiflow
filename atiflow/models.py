from django.db import models
from django.contrib.auth.models import User

class AtiflowModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Comentario(AtiflowModel):
    texto = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' dice: ' + self.texto[:20] + '...'


class Tecnologia(AtiflowModel):
    
    class TipoTecnologia(models.TextChoices):
        LENGUAJE = 'LE', 'Lenguaje'
        FRAMEWORK = 'FR', 'Framework'
        LIBRERIA = 'LI', 'Librería'
        BASE_DE_DATOS = 'BD', 'Base de Datos'
        OTRO = 'OT', 'Otro'

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=2,
        choices=TipoTecnologia.choices,
        default=TipoTecnologia.OTRO
    )
    descripcion = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Sistema(AtiflowModel):
    class TipoAutenticacion(models.TextChoices):
        SIN_AUTENTICACION = 'SA', 'Sin Autenticación'
        PROPIA = 'PR', 'Propia'
        PORTAL_UCAMPUS = 'UC', 'Portal Ucampus'
        U_PASAPORTE = 'UP', 'U-Pasaporte'
        SAU = 'SU', 'SAU'
        OTRA = 'OT', 'Otra'
    class TipoDeSoporte(models.TextChoices):
        ATIDCC = 'AT', 'ATI-DCC'
        SISTEMAS = 'SI', 'Sistemas'
        DESCONOCIDO = 'DE', 'Desconocido'

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    url_repositorio = models.URLField(null=True, blank=True)
    url_test = models.URLField(null=True, blank=True)
    url_produccion = models.URLField(null=True, blank=True)
    url_documentacion = models.URLField(null=True, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, symmetrical=False, default=None, blank=True)
    tipo_autenticacion = models.CharField(
        max_length=2,
        choices=TipoAutenticacion.choices,
        default=TipoAutenticacion.SIN_AUTENTICACION
    )

    tipo_soporte = models.CharField(
        max_length=2,
        choices=TipoDeSoporte.choices,
        default=TipoDeSoporte.DESCONOCIDO
    )
    dependencias = models.ManyToManyField('self', symmetrical=False, blank=True)
    managed = models.BooleanField(default=False)
    tiene_api = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Tarea(AtiflowModel):

    class EstadoTarea(models.TextChoices):
        NO_INICIADA = 'NI', 'No Iniciada'
        EN_ESPERA = 'ES', 'En Espera'
        EN_PROGRESO = 'PR', 'En Progreso'
        TERMINADA = 'TE', 'Terminada'
        CANCELADA = 'CA', 'Cancelada'

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    comentarios = models.ManyToManyField(Comentario, blank=True)
    estado = models.CharField(choices=EstadoTarea.choices, max_length=2, default=EstadoTarea.NO_INICIADA)
    sistemas_afectados = models.ManyToManyField(Sistema, symmetrical=False, blank=True)
    fecha_solicitud = models.DateField()

    def __str__(self):
        return self.titulo
