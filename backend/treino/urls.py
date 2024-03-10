from django.urls import path
from . import views

urlpatterns = [
    path('receber_dados', views.receber_dados),
    path('list_treino/', views.list_treinos),
]