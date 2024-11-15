from django.contrib import admin
from django.utils.html import format_html
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Facultad, ProgramaAcademico

@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'display_color', 'get_decano', 'total_programas')
    search_fields = ('nombre', 'decano__nombre', 'decano__apellido')
    list_select_related = ('decano',)

    def display_color(self, obj):
        return format_html(
            '<span style="background-color: {}; width: 20px; height: 20px; '
            'display: inline-block; margin-right: 10px; vertical-align: middle; '
            'border: 1px solid #ddd;"></span> {}',
            obj.color, obj.color
        )
    display_color.short_description = 'Color'
    display_color.admin_order_field = 'color'

    def get_decano(self, obj):
        if obj.decano:
            return f"{obj.decano.nombre} {obj.decano.apellido}"
        return "Sin decano asignado"
    get_decano.short_description = 'Decano'
    get_decano.admin_order_field = 'decano__nombre'

    def total_programas(self, obj):
        return obj.programaacademico_set.count()
    total_programas.short_description = 'Total Programas'

@admin.register(ProgramaAcademico)
class ProgramaAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_facultad_con_color', 'nivel', 'ciclo', 
                   'snies', 'get_director', 'display_estado_registro')
    list_filter = ('facultad', 'nivel', 'ciclo')
    search_fields = ('nombre', 'snies', 'registro_calificado', 
                    'director__nombre', 'director__apellido')
    list_select_related = ('facultad', 'director')
    
    fieldsets = (
        ('Información Básica', {
            'fields': (
                'nombre',
                ('facultad', 'director'),
                ('nivel', 'ciclo'),
            )
        }),
        ('Información Legal', {
            'fields': (
                ('snies', 'registro_calificado'),
            )
        }),
        ('Plan de Estudios', {
            'fields': ('plan_estudios_formatted',),
            'classes': ('collapse',)
        }),
        ('Características', {
            'fields': ('caracteristicas_formatted',),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('plan_estudios_formatted', 'caracteristicas_formatted')

    def get_facultad_con_color(self, obj):
        return format_html(
            '<span style="background-color: {}; width: 10px; height: 10px; '
            'display: inline-block; margin-right: 5px; border-radius: 50%;"></span> {}',
            obj.facultad.color, obj.facultad.nombre
        )
    get_facultad_con_color.short_description = 'Facultad'
    get_facultad_con_color.admin_order_field = 'facultad__nombre'

    def get_director(self, obj):
        if obj.director:
            return f"{obj.director.nombre} {obj.director.apellido}"
        return "Sin director asignado"
    get_director.short_description = 'Director'
    get_director.admin_order_field = 'director__nombre'

    def display_estado_registro(self, obj):
        # Aquí podrías implementar lógica para verificar vigencia del registro
        return format_html(
            '<span class="registro-activo">Registro Activo</span>'
        )
    display_estado_registro.short_description = 'Estado Registro'

    def plan_estudios_formatted(self, obj):
        return format_html('<pre style="max-height: 400px; overflow-y: auto;">{}</pre>',
            json.dumps(obj.plan_estudios, indent=2, ensure_ascii=False, cls=DjangoJSONEncoder))
    plan_estudios_formatted.short_description = 'Plan de Estudios'

    def caracteristicas_formatted(self, obj):
        return format_html('<pre style="max-height: 400px; overflow-y: auto;">{}</pre>',
            json.dumps(obj.caracteristicas, indent=2, ensure_ascii=False, cls=DjangoJSONEncoder))
    caracteristicas_formatted.short_description = 'Características'

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }