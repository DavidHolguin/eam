from django.contrib import admin
from django.utils.html import format_html
from .models import Pipeline, Step, Lead

@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'total_steps', 'total_leads')
    search_fields = ('nombre', 'descripcion')
    
    def total_steps(self, obj):
        return obj.step_set.count()
    total_steps.short_description = 'Total de Pasos'
    
    def total_leads(self, obj):
        return obj.lead_set.count()
    total_leads.short_description = 'Total de Leads'

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pipeline', 'orden', 'display_requisitos', 'total_leads')
    list_filter = ('pipeline',)
    search_fields = ('nombre', 'pipeline__nombre')
    ordering = ('pipeline', 'orden')
    
    def display_requisitos(self, obj):
        return format_html("<pre>{}</pre>", obj.requisitos)
    display_requisitos.short_description = 'Requisitos'
    
    def total_leads(self, obj):
        return obj.lead_set.count()
    total_leads.short_description = 'Leads en este paso'

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'pipeline', 'step_actual', 'asesor', 'score', 'fecha_ingreso')
    list_filter = ('pipeline', 'step_actual', 'asesor')
    search_fields = ('estudiante__nombre', 'asesor__nombre', 'pipeline__nombre')
    readonly_fields = ('fecha_ingreso',)
    list_select_related = ('estudiante', 'pipeline', 'step_actual', 'asesor')
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('estudiante', 'pipeline', 'step_actual', 'asesor')
        }),
        ('Métricas', {
            'fields': ('score', 'fecha_ingreso')
        }),
        ('Seguimiento', {
            'fields': ('datos_seguimiento',),
            'classes': ('collapse',)
        })
    )