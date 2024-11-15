# views.py
from django.utils import timezone
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Persona
from .serializers import PersonaSerializer, PersonaListSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rol', 'activo']
    search_fields = ['nombres', 'apellidos', 'numero_documento', 'email_institucional']
    ordering_fields = ['fecha_vinculacion', 'apellidos']

    def get_serializer_class(self):
        if self.action == 'list':
            return PersonaListSerializer
        return PersonaSerializer

    def perform_create(self, serializer):
        serializer.save(fecha_vinculacion=timezone.now().date())

    @action(detail=False)
    def decanos(self, request):
        decanos = self.get_queryset().filter(rol='DECANO', activo=True)
        serializer = self.get_serializer(decanos, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def directores(self, request):
        directores = self.get_queryset().filter(rol='DIRECTOR', activo=True)
        serializer = self.get_serializer(directores, many=True)
        return Response(serializer.data)