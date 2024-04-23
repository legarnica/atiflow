from django.contrib import admin

# Register your models here.

from .models import Comentario, Sistema, Tarea, Tecnologia

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_autenticacion', 'tipo_soporte')
    search_fields = ['nombre']
    list_per_page = 10

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'fecha_solicitud')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    pass
