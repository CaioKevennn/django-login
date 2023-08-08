from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [
   path('login/', views.login, name='login'),
   path('cadastro/',views.cadastro,name='cadastro'),
   path('valid_cad/',views.valid_cad, name='valid_cad'),
   path('valid_log/',views.valid_log, name='valid_log'),
   path('sair',views.sair,name="sair")

]