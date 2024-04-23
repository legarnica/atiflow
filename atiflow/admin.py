from django.contrib import admin

# Register your models here.

from .models import Comentario, EstadoTarea, Sistema, Tarea, Tecnologia

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(EstadoTarea)
class EstadoTareaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_autenticacion', 'tipo_soporte')
    search_fields = ['nombre']
    list_per_page = 10

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    pass
