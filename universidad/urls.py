# universidad/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversidadViewSet, ItemInformacionViewSet

router = DefaultRouter()
router.register(r'universidades', UniversidadViewSet)
router.register(r'items-informacion', ItemInformacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]