from django.db import models

class Facultad(models.Model):
    """
    Representa una facultad dentro de una universidad, con información sobre su nombre, color representativo y decano.

    Attributes:
        nombre (str): Nombre de la facultad.
        color (str): Código de color hexadecimal representativo de la facultad.
        decano (ForeignKey): Referencia a la persona que ocupa el cargo de decano, perteneciente al modelo `Persona` en la aplicación `team`.

    Relations:
        - Persona (decano): Relación de uno a uno con el modelo `Persona`, representando el decano de la facultad.

    Examples:
        ```python
        # Creación de una facultad
        facultad = Facultad.objects.create(
            nombre="Facultad de Ciencias",
            color="#0055FF",
            decano=persona_decano
        )
        ```

    Notes:
        - `decano` se puede establecer como `null` para facultades sin decano actual.
        - Asegurarse de que el color esté en formato hexadecimal para la consistencia visual.
    """
    nombre = models.CharField(max_length=200)
    color = models.CharField(max_length=7)
    decano = models.ForeignKey('team.Persona', on_delete=models.SET_NULL, null=True)


class ProgramaAcademico(models.Model):
    """
    Representa un programa académico asociado a una facultad, con información de nivel académico, ciclo y detalles específicos.

    Attributes:
        facultad (ForeignKey): Facultad a la que pertenece el programa académico.
        nombre (str): Nombre del programa académico.
        snies (str): Código SNIES único del programa.
        registro_calificado (str): Código de registro calificado del programa.
        nivel (str): Nivel académico del programa (e.g., pregrado, posgrado).
        ciclo (str): Ciclo de formación del programa.
        director (ForeignKey): Referencia a la persona que dirige el programa, del modelo `Persona`.
        plan_estudios (JSON): Detalles estructurados del plan de estudios.
        caracteristicas (JSON): Información adicional sobre el programa, como objetivos, perfil de egreso, etc.

    Relations:
        - Facultad: Relación de muchos a uno con el modelo `Facultad`, indicando a qué facultad pertenece el programa.
        - Persona (director): Relación de uno a uno con el modelo `Persona`, representando al director del programa.

    Examples:
        ```python
        # Creación de un programa académico
        programa = ProgramaAcademico.objects.create(
            facultad=facultad,
            nombre="Ingeniería de Sistemas",
            snies="123456",
            registro_calificado="RC-2024-56789",
            nivel="Pregrado",
            ciclo="Profesional",
            director=persona_director,
            plan_estudios={"semestres": 10, "cursos": ["Algoritmos", "Matemáticas", "Física"]},
            caracteristicas={"modalidad": "Presencial", "duracion": "5 años"}
        )
        ```

    Notes:
        - El atributo `plan_estudios` permite organizar y almacenar la estructura del programa.
        - `caracteristicas` es útil para incluir información específica del programa, que puede ser utilizada para mostrar al público o para fines internos.
    """
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    snies = models.CharField(max_length=20)
    registro_calificado = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20)
    ciclo = models.CharField(max_length=20)
    director = models.ForeignKey('team.Persona', on_delete=models.SET_NULL, null=True)
    plan_estudios = models.JSONField()
    caracteristicas = models.JSONField()
