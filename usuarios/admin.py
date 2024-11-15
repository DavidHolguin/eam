from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario, Asesor

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo', 'is_active', 'date_joined')
    list_filter = ('tipo', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información Personal'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Rol de Usuario'), {'fields': ('tipo',)}),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'tipo', 'email', 'first_name', 'last_name'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Hace que ciertos campos sean de solo lectura después de la creación"""
        if obj:  # Si el objeto ya existe
            return ['date_joined', 'last_login']
        return []

class AsesorInline(admin.StackedInline):
    """Inline admin para el modelo Asesor"""
    model = Asesor
    can_delete = False
    verbose_name_plural = 'Información de Asesor'

@admin.register(Asesor)
class AsesorAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_full_name', 'especialidad')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'especialidad')
    list_filter = ('especialidad',)
    
    def get_username(self, obj):
        return obj.usuario.username
    get_username.short_description = 'Usuario'
    get_username.admin_order_field = 'usuario__username'
    
    def get_full_name(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}".strip()
    get_full_name.short_description = 'Nombre Completo'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Filtra los usuarios disponibles para mostrar solo los de tipo asesor"""
        if db_field.name == "usuario":
            kwargs["queryset"] = Usuario.objects.filter(tipo='asesor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_inline_instances(self, request, obj=None):
        """No muestra inlines en la página de creación"""
        if not obj:
            return []
        return super().get_inline_instances(request, obj)

# Modificar el UsuarioAdmin para incluir el inline de Asesor
UsuarioAdmin.inlines = [AsesorInline]