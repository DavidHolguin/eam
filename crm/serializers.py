# crm/serializers.py
from rest_framework import serializers
from .models import Pipeline, Step, Lead

class PipelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipeline
        fields = ['id', 'nombre', 'descripcion']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'pipeline', 'nombre', 'orden', 'requisitos']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'estudiante', 'pipeline', 'step_actual', 'asesor',
                 'score', 'fecha_ingreso', 'datos_seguimiento']
