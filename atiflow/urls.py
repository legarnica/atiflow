from django.urls import path


from .views import TareaDetailView

app_name = 'atiflow'

urlpatterns = [
    path('tarea/<int:pk>/', TareaDetailView.as_view(), name='tarea_detail'),
]