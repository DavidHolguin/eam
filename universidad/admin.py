from django.contrib import admin
from django.utils.html import format_html
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import Universidad, ItemInformacion

@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_nit', 'mostrar_logros')
    search_fields = ('nombre', 'datos_legales', 'historia')
    list_filter = ('logros',)
    
    def mostrar_nit(self, obj):
        """Muestra el NIT desde el campo datos_legales"""
        return obj.datos_legales.get('nit', 'No especificado')
    mostrar_nit.short_description = 'NIT'
    
    def mostrar_logros(self, obj):
        """Formatea los logros como una lista HTML"""
        logros_html = '<br>'.join([f'• {logro}' for logro in obj.logros])
        return format_html(logros_html)
    mostrar_logros.short_description = 'Logros'
    
    def get_form(self, request, obj=None, **kwargs):
        """Personaliza el formulario para mostrar los campos JSON como texto formateado"""
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['datos_legales'].initial = json.dumps(
                obj.datos_legales, indent=2, cls=DjangoJSONEncoder
            )
            form.base_fields['logros'].initial = json.dumps(
                obj.logros, indent=2, cls=DjangoJSONEncoder
            )
        return form

@admin.register(ItemInformacion)
class ItemInformacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'universidad', 'tipo', 'mostrar_etiquetas', 'fecha_creacion')
    list_filter = ('universidad', 'tipo', 'fecha_creacion')
    search_fields = ('titulo', 'contenido', 'etiquetas')
    readonly_fields = ('fecha_creacion',)
    
    def mostrar_etiquetas(self, obj):
        """Muestra las etiquetas como badges HTML"""
        etiquetas_html = ' '.join([
            f'<span style="background-color: #e2e8f0; padding: 2px 6px; '
            f'border-radius: 10px; margin: 0 2px;">{etiqueta}</span>'
            for etiqueta in obj.etiquetas
        ])
        return format_html(etiquetas_html)
    mostrar_etiquetas.short_description = 'Etiquetas'
    
    def get_form(self, request, obj=None, **kwargs):
        """Personaliza el formulario para mostrar los campos JSON como texto formateado"""
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['contenido'].initial = json.dumps(
                obj.contenido, indent=2, cls=DjangoJSONEncoder
            )
            form.base_fields['etiquetas'].initial = json.dumps(
                obj.etiquetas, indent=2, cls=DjangoJSONEncoder
            )
        return form