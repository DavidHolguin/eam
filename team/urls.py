# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'personas', views.PersonaViewSet)

app_name = 'team'

urlpatterns = [
    path('', include(router.urls)),
]