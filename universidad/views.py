# universidad/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Universidad, ItemInformacion
from .serializers import UniversidadSerializer, ItemInformacionSerializer

class UniversidadViewSet(viewsets.ModelViewSet):
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer
    permission_classes = [IsAuthenticated]

class ItemInformacionViewSet(viewsets.ModelViewSet):
    queryset = ItemInformacion.objects.all()
    serializer_class = ItemInformacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ItemInformacion.objects.all()
        universidad_id = self.request.query_params.get('universidad', None)
        if universidad_id is not None:
            queryset = queryset.filter(universidad_id=universidad_id)
        return queryset