# models.py
from django.db import models
from django.core.validators import RegexValidator

class Persona(models.Model):
    TIPOS_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PS', 'Pasaporte'),
    ]
    
    ROLES = [
        ('DECANO', 'Decano'),
        ('DIRECTOR', 'Director de Programa'),
        ('DOCENTE', 'Docente'),
        ('ADMINISTRATIVO', 'Personal Administrativo'),
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=TIPOS_DOCUMENTO)
    numero_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    email_institucional = models.EmailField(unique=True)
    email_personal = models.EmailField(blank=True)
    rol = models.CharField(max_length=20, choices=ROLES)
    fecha_vinculacion = models.DateField()
    activo = models.BooleanField(default=True)
    titulo_academico = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    cv_resumen = models.TextField()
    foto = models.ImageField(upload_to='team/fotos/', null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['apellidos', 'nombres']
        indexes = [
            models.Index(fields=['numero_documento']),
            models.Index(fields=['email_institucional']),
            models.Index(fields=['rol']),
        ]

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"