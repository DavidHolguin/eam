# crm/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PipelineViewSet, StepViewSet, LeadViewSet

router = DefaultRouter()
router.register(r'pipelines', PipelineViewSet)
router.register(r'steps', StepViewSet)
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]