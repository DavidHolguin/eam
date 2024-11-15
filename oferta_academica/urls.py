# oferta_academica/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultadViewSet, ProgramaAcademicoViewSet

router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'programas', ProgramaAcademicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]