# estudiantes/serializers.py
from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'usuario', 'programa', 'etapa', 'referido_por']