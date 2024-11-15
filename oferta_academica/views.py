# oferta_academica/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Facultad, ProgramaAcademico
from .serializers import FacultadSerializer, ProgramaAcademicoSerializer

class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer
    permission_classes = [IsAuthenticated]

class ProgramaAcademicoViewSet(viewsets.ModelViewSet):
    queryset = ProgramaAcademico.objects.all()
    serializer_class = ProgramaAcademicoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ProgramaAcademico.objects.all()
        facultad_id = self.request.query_params.get('facultad', None)
        if facultad_id is not None:
            queryset = queryset.filter(facultad_id=facultad_id)
        return queryset