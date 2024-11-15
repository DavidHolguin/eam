# usuarios/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Usuario, Asesor
from .serializers import UsuarioSerializer, AsesorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class AsesorViewSet(viewsets.ModelViewSet):
    queryset = Asesor.objects.all()
    serializer_class = AsesorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Asesor.objects.all()
        especialidad = self.request.query_params.get('especialidad', None)
        if especialidad is not None:
            queryset = queryset.filter(especialidad=especialidad)
        return queryset