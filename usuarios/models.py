from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
    Extiende el modelo de usuario de Django para incluir un tipo de usuario específico, como estudiante, asesor o administrador.

    Attributes:
        tipo (str): Tipo de usuario, con opciones: 'estudiante', 'asesor' y 'admin'.

    Relations:
        - Asesor: Relación de uno a uno con el modelo `Asesor` para usuarios de tipo asesor.

    Examples:
        ```python
        # Creación de un usuario de tipo asesor
        usuario = Usuario.objects.create_user(
            username="usuario_asesor",
            password="contraseña123",
            tipo="asesor"
        )
        ```

    Notes:
        - Utiliza el sistema de autenticación de Django, por lo que hereda atributos y métodos como `username`, `password`, `is_staff`, etc.
        - `tipo` permite clasificar el usuario según su rol dentro del sistema.
    """
    tipo = models.CharField(max_length=20, choices=[('estudiante', 'Estudiante'), ('asesor', 'Asesor'), ('admin', 'Administrador')])


class Asesor(models.Model):
    """
    Representa información adicional para un usuario de tipo asesor, incluyendo su especialidad.

    Attributes:
        usuario (OneToOneField): Referencia al usuario correspondiente, de tipo asesor.
        especialidad (str): Especialidad o área de experiencia del asesor.

    Relations:
        - Usuario: Relación de uno a uno con el modelo `Usuario`, vinculando al usuario asesor con su información específica.

    Examples:
        ```python
        # Creación de un perfil de asesor para un usuario existente
        asesor = Asesor.objects.create(
            usuario=usuario,
            especialidad="Matemáticas"
        )
        ```

    Notes:
        - Este modelo depende de que el `Usuario` esté marcado como `tipo="asesor"`.
        - `especialidad` permite almacenar información relevante sobre el área de conocimiento o experiencia del asesor.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
