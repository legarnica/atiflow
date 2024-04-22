from django.db import models
from django.contrib.auth.models import User

class AtiflowModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Comentario(AtiflowModel):
    detalle = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Sistema(AtiflowModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    url_repositorio = models.URLField()
    url_test = models.URLField()
    url_produccion = models.URLField()
    url_documentacion = models.URLField()

class EstadoTarea(AtiflowModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Tarea(AtiflowModel):
    titulo = models.CharField(max_length=100)
    comentarios = models.ManyToManyField(Comentario)
    estado = models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)
