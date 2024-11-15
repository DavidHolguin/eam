# universidad/serializers.py
from rest_framework import serializers
from .models import Universidad, ItemInformacion

class UniversidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidad
        fields = ['id', 'nombre', 'datos_legales', 'historia', 'logros']

class ItemInformacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInformacion
        fields = ['id', 'universidad', 'titulo', 'contenido', 'tipo', 'etiquetas', 'fecha_creacion']
