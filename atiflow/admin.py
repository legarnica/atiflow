from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
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
    list_display = ('titulo', 'estado', 'fecha_solicitud', 'detail_view_link')
    search_fields = ('nombre',)
    list_filter = ('estado','fecha_solicitud',)

    def detail_view_link(self, obj):
        url = reverse('atiflow:tarea_detail', args=(obj.pk,))
        return format_html('<a href="{}">Ver Detalles</a>', url)
    
    detail_view_link.short_description = 'Ver Detalles'



@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    pass
