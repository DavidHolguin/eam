from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('get_nombre_completo', 'get_email', 'get_programa', 'etapa', 
                   'get_referido_por', 'total_referidos', 'get_estado')
    list_filter = ('etapa', 'programa', 'programa__facultad')
    search_fields = (
        'usuario__nombre', 
        'usuario__apellido',
        'usuario__email',
        'programa__nombre'
    )
    autocomplete_fields = ['programa', 'referido_por']
    readonly_fields = ('total_referidos',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': (
                'usuario',
                ('programa', 'etapa'),
            )
        }),
        ('Sistema de Referidos', {
            'fields': (
                'referido_por',
                'total_referidos',
            ),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        # Optimizar consultas y agregar conteo de referidos
        return super().get_queryset(request)\
            .select_related('usuario', 'programa', 'referido_por', 'programa__facultad')\
            .annotate(num_referidos=Count('referidos'))

    def get_nombre_completo(self, obj):
        return f"{obj.usuario.nombre} {obj.usuario.apellido}"
    get_nombre_completo.short_description = 'Nombre Completo'
    get_nombre_completo.admin_order_field = 'usuario__nombre'

    def get_email(self, obj):
        return obj.usuario.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'usuario__email'

    def get_programa(self, obj):
        if obj.programa:
            return f"{obj.programa.nombre} - {obj.programa.facultad.nombre}"
        return "Sin programa"
    get_programa.short_description = 'Programa Académico'
    get_programa.admin_order_field = 'programa__nombre'

    def get_referido_por(self, obj):
        if obj.referido_por:
            return f"{obj.referido_por.usuario.nombre} {obj.referido_por.usuario.apellido}"
        return "Sin referido"
    get_referido_por.short_description = 'Referido Por'
    get_referido_por.admin_order_field = 'referido_por__usuario__nombre'

    def total_referidos(self, obj):
        return obj.num_referidos
    total_referidos.short_description = 'Total Referidos'
    total_referidos.admin_order_field = 'num_referidos'

    def get_estado(self, obj):
        colors = {
            'interesado': '#FFA500',  # Naranja
            'registrado': '#4169E1',  # Azul real
            'aspirante': '#9370DB',   # Púrpura medio
            'matriculado': '#20B2AA', # Verde azulado claro
            'estudiante': '#228B22'   # Verde bosque
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 3px; font-weight: bold;">{}</span>',
            colors.get(obj.etapa, '#808080'),
            obj.get_etapa_display()
        )
    get_estado.short_description = 'Estado'
    get_estado.admin_order_field = 'etapa'

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }