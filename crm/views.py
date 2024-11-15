# crm/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Pipeline, Step, Lead
from .serializers import PipelineSerializer, StepSerializer, LeadSerializer

class PipelineViewSet(viewsets.ModelViewSet):
    queryset = Pipeline.objects.all()
    serializer_class = PipelineSerializer
    permission_classes = [IsAuthenticated]

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Step.objects.all()
        pipeline_id = self.request.query_params.get('pipeline', None)
        if pipeline_id is not None:
            queryset = queryset.filter(pipeline_id=pipeline_id)
        return queryset

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Lead.objects.all()
        asesor_id = self.request.query_params.get('asesor', None)
        if asesor_id is not None:
            queryset = queryset.filter(asesor_id=asesor_id)
        return queryset