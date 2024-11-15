# serializers.py
from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
        read_only_fields = ('fecha_vinculacion',)

    def validate_email_institucional(self, value):
        """Validar que el email institucional tenga el dominio correcto"""
        if not value.endswith('@institucion.edu.co'):
            raise serializers.ValidationError(
                "El email institucional debe ser del dominio @institucion.edu.co"
            )
        return value

class PersonaListSerializer(serializers.ModelSerializer):
    """Serializer ligero para listados"""
    class Meta:
        model = Persona
        fields = ('id', 'nombres', 'apellidos', 'rol', 'titulo_academico', 'foto')