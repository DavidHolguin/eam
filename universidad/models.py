from django.db import models

class Universidad(models.Model):
    """
    Representa una institución universitaria.

    Attributes:
        nombre (str): Nombre oficial de la universidad.
        datos_legales (dict): Información legal de la institución.
        historia (str): Reseña histórica de la universidad.
        logros (list): Lista de logros destacados de la institución.

    Methods:
        __str__(): Retorna el nombre de la universidad.

    Examples:
        <code>
        # Crear una nueva universidad
        uni = Universidad.objects.create(
            nombre="Universidad EAM",
            datos_legales={"nit": "123456789", "resolucion": "001-2024"},
            historia="Fundada en 1970...",
            logros=["Acreditación de Alta Calidad", "Premio Nacional de Educación"]
        )
        </code>

    Notes:
        - Los datos_legales y logros se almacenan como JSONField para flexibilidad.
        - Considerar añadir campos para contacto y ubicación en futuras iteraciones.
    """
    nombre = models.CharField(max_length=200)
    datos_legales = models.JSONField()
    historia = models.TextField()
    logros = models.JSONField()

    def __str__(self):
        return self.nombre

class ItemInformacion(models.Model):
    """
    Almacena elementos de información relacionados con una universidad.

    Attributes:
        universidad (Universidad): Universidad a la que pertenece el item.
        titulo (str): Título del item de información.
        contenido (dict): Contenido detallado del item.
        tipo (str): Categoría o tipo de información.
        etiquetas (list): Lista de etiquetas para categorización.
        fecha_creacion (datetime): Fecha y hora de creación del item.

    Relations:
        - Universidad: Relación many-to-one con el modelo Universidad.

    Methods:
        __str__(): Retorna el título del item de información.

    Examples:
        <code>
        # Crear un nuevo item de información
        item = ItemInformacion.objects.create(
            universidad=Universidad.objects.get(nombre="Universidad EAM"),
            titulo="Proceso de Admisión 2025",
            contenido={"pasos": ["Registro en línea", "Examen de ingreso", "Entrevista"]},
            tipo="Admisiones",
            etiquetas=["admisión", "nuevos estudiantes", "2025"]
        )
        </code>

    Notes:
        - El campo contenido permite almacenar estructuras de datos complejas.
        - Las etiquetas facilitan la búsqueda y filtrado de información.
    """
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.JSONField()
    tipo = models.CharField(max_length=50)
    etiquetas = models.JSONField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
