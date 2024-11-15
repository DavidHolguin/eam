# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario, Asesor

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'tipo']
        extra_kwargs = {'password': {'write_only': True}}

class AsesorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Asesor
        fields = ['id', 'usuario', 'especialidad']
