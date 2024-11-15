# usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AsesorViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'asesores', AsesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]