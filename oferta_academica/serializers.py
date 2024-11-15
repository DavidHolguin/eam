# oferta_academica/serializers.py
from rest_framework import serializers
from .models import Facultad, ProgramaAcademico

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ['id', 'nombre', 'color', 'decano']

class ProgramaAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaAcademico
        fields = ['id', 'facultad', 'nombre', 'snies', 'registro_calificado', 
                 'nivel', 'ciclo', 'director', 'plan_estudios', 'caracteristicas']
