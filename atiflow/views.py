from django.shortcuts import render
from django.views.generic import DetailView

from .models import Tarea


class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'atiflow/tarea_detail.html'

