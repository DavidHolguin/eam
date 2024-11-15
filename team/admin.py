from django.contrib import admin
from django.utils.html import format_html
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
import json
from datetime import date
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('foto_preview', 'nombre_completo', 'rol_badge', 'titulo_academico', 
                   'email_institucional', 'telefono_formato', 'edad', 
                   'tiempo_vinculacion', 'estado_activo')
    
    list_filter = ('rol', 'activo', 'tipo_documento')
    search_fields = ('nombres', 'apellidos', 'numero_documento', 
                    'email_institucional', 'email_personal', 
                    'titulo_academico', 'especialidad')
    
    readonly_fields = ('foto_preview_large', 'edad', 'tiempo_vinculacion')
    
    fieldsets = (
        ('Información Personal', {
            'fields': (
                ('nombres', 'apellidos'),
                ('tipo_documento', 'numero_documento'),
                'fecha_nacimiento',
                ('telefono', 'edad'),
                ('email_institucional', 'email_personal'),
            )
        }),
        ('Información Profesional', {
            'fields': (
                'rol',
                ('titulo_academico', 'especialidad'),
                ('fecha_vinculacion', 'tiempo_vinculacion'),
                'activo',
            )
        }),
        ('Perfil Profesional', {
            'fields': (
                'cv_resumen',
                ('foto', 'foto_preview_large'),
            ),
            'classes': ('collapse',)
        }),
        ('Información Adicional', {
            'fields': ('metadata_formatted',),
            'classes': ('collapse',)
        }),
    )
    
    def foto_preview(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; '
                'object-fit: cover; border: 2px solid #ddd;">', obj.foto.url
            )
        return format_html(
            '<div style="width: 40px; height: 40px; border-radius: 50%; '
            'background-color: #eee; display: flex; align-items: center; '
            'justify-content: center; border: 2px solid #ddd;">?</div>'
        )
    foto_preview.short_description = 'Foto'

    def foto_preview_large(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; '
                'border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">', 
                obj.foto.url
            )
        return "Sin foto"
    foto_preview_large.short_description = 'Vista previa de foto'

    def rol_badge(self, obj):
        colors = {
            'DECANO': '#DC3545',        # Rojo
            'DIRECTOR': '#FD7E14',      # Naranja
            'DOCENTE': '#28A745',       # Verde
            'ADMINISTRATIVO': '#17A2B8'  # Azul
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 8px; '
            'border-radius: 4px; font-size: 0.8em; font-weight: bold;">{}</span>',
            colors.get(obj.rol, '#6C757D'),
            obj.get_rol_display()
        )
    rol_badge.short_description = 'Rol'
    rol_badge.admin_order_field = 'rol'

    def telefono_formato(self, obj):
        return format_html('<span style="font-family: monospace;">{}</span>', obj.telefono)
    telefono_formato.short_description = 'Teléfono'
    telefono_formato.admin_order_field = 'telefono'

    def edad(self, obj):
        today = date.today()
        edad = today.year - obj.fecha_nacimiento.year - \
               ((today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))
        return f"{edad} años"
    edad.short_description = 'Edad'

    def tiempo_vinculacion(self, obj):
        today = date.today()
        years = today.year - obj.fecha_vinculacion.year - \
                ((today.month, today.day) < (obj.fecha_vinculacion.month, obj.fecha_vinculacion.day))
        months = (today.month - obj.fecha_vinculacion.month) % 12
        if years == 0:
            return f"{months} meses"
        return f"{years} años, {months} meses"
    tiempo_vinculacion.short_description = 'Tiempo de Vinculación'

    def estado_activo(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            '#28A745' if obj.activo else '#DC3545',
            'Activo' if obj.activo else 'Inactivo'
        )
    estado_activo.short_description = 'Estado'
    estado_activo.admin_order_field = 'activo'

    def metadata_formatted(self, obj):
        return format_html(
            '<pre style="max-height: 300px; overflow-y: auto;">{}</pre>',
            json.dumps(obj.metadata, indent=2, ensure_ascii=False, cls=DjangoJSONEncoder)
        )
    metadata_formatted.short_description = 'Metadata'

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }