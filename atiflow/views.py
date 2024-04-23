from django.shortcuts import render
from django.views.generic import DetailView

from .models import Tarea


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'atiflow/tarea_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        print(id)
        context['tarea'] = 'Detalle de Tarea'
        return context
