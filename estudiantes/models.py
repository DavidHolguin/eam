from django.db import models

class Estudiante(models.Model):
    """
    Representa un estudiante en el sistema, con información sobre su programa académico, etapa en el proceso de admisión y referencia.

    Attributes:
        usuario (OneToOneField): Referencia al usuario correspondiente en el modelo `Usuario`.
        programa (ForeignKey): Programa académico en el que el estudiante está interesado o matriculado, del modelo `ProgramaAcademico`.
        etapa (str): Etapa actual del estudiante en el proceso de admisión, con opciones como 'interesado', 'registrado', 'aspirante', 'matriculado', y 'estudiante'.
        referido_por (ForeignKey): Referencia opcional a otro estudiante que haya referido a este estudiante.

    Relations:
        - Usuario: Relación de uno a uno con el modelo `Usuario`, representando la información básica de autenticación y perfil.
        - ProgramaAcademico: Relación de muchos a uno con el modelo `ProgramaAcademico`, indicando el programa en el que el estudiante está involucrado.
        - Estudiante (referido_por): Relación de muchos a uno consigo mismo, representando al estudiante que refirió al actual.

    Examples:
        ```python
        # Creación de un estudiante con referencia a otro estudiante
        estudiante_referido = Estudiante.objects.create(
            usuario=usuario,
            programa=programa,
            etapa="registrado",
            referido_por=referente
        )
        ```

    Notes:
        - `etapa` indica la situación del estudiante en el flujo de admisión y progreso académico.
        - `referido_por` permite crear un sistema de referencias entre estudiantes, lo cual puede ser útil para seguimiento o beneficios de referencia.
    """
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    programa = models.ForeignKey('oferta_academica.ProgramaAcademico', on_delete=models.SET_NULL, null=True)
    etapa = models.CharField(max_length=20, choices=[('interesado', 'Interesado'), ('registrado', 'Registrado'), ('aspirante', 'Aspirante'), ('matriculado', 'Matriculado'), ('estudiante', 'Estudiante EAM')])
    referido_por = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='referidos')
