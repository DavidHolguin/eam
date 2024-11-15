from django.db import models

class Pipeline(models.Model):
    """
    Representa un flujo de trabajo o pipeline que contiene una serie de pasos (steps) para guiar el proceso de un lead.

    Attributes:
        nombre (str): Nombre del pipeline, identificando el flujo de trabajo.
        descripcion (str): Descripción detallada del pipeline y su propósito.

    Relations:
        - Step: Relación de uno a muchos con el modelo `Step`, representando los pasos en el pipeline.
        - Lead: Relación de uno a muchos con el modelo `Lead`, indicando los leads asignados a este pipeline.

    Examples:
        ```python
        # Creación de un pipeline
        pipeline = Pipeline.objects.create(
            nombre="Pipeline de Admisiones",
            descripcion="Proceso de admisiones para estudiantes interesados"
        )
        ```

    Notes:
        - Cada pipeline puede tener varios pasos en una secuencia específica.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class Step(models.Model):
    """
    Representa un paso dentro de un pipeline, indicando un estado o actividad en el proceso.

    Attributes:
        pipeline (ForeignKey): Pipeline al que pertenece el paso.
        nombre (str): Nombre descriptivo del paso.
        orden (int): Orden del paso dentro del pipeline.
        requisitos (JSON): Lista o diccionario de requisitos para completar el paso.

    Relations:
        - Pipeline: Relación de muchos a uno con `Pipeline`, representando el flujo al que pertenece el paso.
        - Lead (step_actual): Relación de uno a muchos con `Lead`, donde los leads pueden estar en un paso específico.

    Examples:
        ```python
        # Creación de un step en el pipeline
        step = Step.objects.create(
            pipeline=pipeline,
            nombre="Entrevista inicial",
            orden=1,
            requisitos={"documentos": ["identificación", "calificaciones"]}
        )
        ```

    Notes:
        - `orden` define el flujo secuencial en el pipeline.
        - `requisitos` permite almacenar condiciones específicas para cada paso.
    """
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    orden = models.IntegerField()
    requisitos = models.JSONField()


class Lead(models.Model):
    """
    Representa un lead, es decir, un estudiante en proceso dentro de un pipeline específico, con un seguimiento de su progreso.

    Attributes:
        estudiante (ForeignKey): Estudiante asignado al lead, del modelo `Estudiante`.
        pipeline (ForeignKey): Pipeline en el que se encuentra el lead.
        step_actual (ForeignKey): Paso actual del pipeline en el que se encuentra el lead.
        asesor (ForeignKey): Asesor asignado al lead, del modelo `Asesor`.
        score (float): Puntaje o calificación actual del lead.
        fecha_ingreso (DateTime): Fecha y hora de ingreso del lead al pipeline.
        datos_seguimiento (JSON): Información estructurada de seguimiento del lead, como notas y actividades realizadas.

    Relations:
        - Estudiante: Relación de muchos a uno con `Estudiante`, indicando el estudiante asignado.
        - Pipeline: Relación de muchos a uno con `Pipeline`, indicando el proceso en el que se encuentra el lead.
        - Step: Relación de muchos a uno con `Step`, representando el paso actual del lead en el pipeline.
        - Asesor: Relación de muchos a uno con `Asesor`, indicando el asesor responsable.

    Examples:
        ```python
        # Creación de un lead
        lead = Lead.objects.create(
            estudiante=estudiante,
            pipeline=pipeline,
            step_actual=step,
            asesor=asesor,
            score=85.5,
            datos_seguimiento={"notas": ["Entrevista completa", "Documentos revisados"]}
        )
        ```

    Notes:
        - `step_actual` permite rastrear el avance del lead en el pipeline.
        - `datos_seguimiento` es útil para almacenar notas, fechas y otros detalles importantes.
    """
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE)
    step_actual = models.ForeignKey(Step, on_delete=models.CASCADE)
    asesor = models.ForeignKey('usuarios.Asesor', on_delete=models.SET_NULL, null=True)
    score = models.FloatField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    datos_seguimiento = models.JSONField()
