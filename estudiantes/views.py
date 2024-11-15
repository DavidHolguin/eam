# estudiantes/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Estudiante.objects.all()
        programa_id = self.request.query_params.get('programa', None)
        etapa = self.request.query_params.get('etapa', None)
        
        if programa_id is not None:
            queryset = queryset.filter(programa_id=programa_id)
        if etapa is not None:
            queryset = queryset.filter(etapa=etapa)
            
        return queryset