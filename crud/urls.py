from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('home/', views.paginaInicial, name='pagina-inicial'),
]
