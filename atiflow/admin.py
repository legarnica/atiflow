from django.contrib import admin

# Register your models here.

from .models import Comentario, EstadoTarea, Sistema, Tarea

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(EstadoTarea)
class EstadoTareaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sistema)
class SistemaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    pass
