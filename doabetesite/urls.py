from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('home', views.home, name='home'),
    path('registro', views.registro, name='paginaregistro'),
    path('login', views.login, name='paginalogin'),
    path('sobre', views.sobre, name='paginasobre'),
    path('contato', views.contato, name='paginacontato'),
    path('produtos', views.produtos, name='paginaprodutos'),
]