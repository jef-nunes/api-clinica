"""
URL configuration for projeto_clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_pacientes.api.viewsets import PacientesViewSet
from app_agendamentos.api.viewsets import AgendamentoViewSet
from app_historicos.api.viewsets import HistoricosViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'historicos', HistoricosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
