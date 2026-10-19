from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_aprendices, name='listar_aprendices'),
]
