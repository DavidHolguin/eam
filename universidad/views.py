# universidad/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .models import Universidad, ItemInformacion
from .serializers import UniversidadSerializer, ItemInformacionSerializer

class ReadOnlyIfGet(BasePermission):
    """
    ReadOnlyIfGet
    -------------
    Permiso personalizado que permite acceso público para métodos seguros (solo lectura), 
    mientras que los métodos de escritura requieren autenticación.

    Attributes:
        - SAFE_METHODS (tuple): Métodos HTTP considerados seguros ('GET', 'HEAD', 'OPTIONS').

    Methods:
        has_permission(request, view): Evalúa si el usuario tiene permiso para realizar la solicitud. 
            Permite acceso sin autenticación para métodos seguros, requiere autenticación para los demás.

    Examples:
        ```python
        # Acceso sin autenticación para GET
        GET /api/items_informacion/

        # Requiere autenticación para POST
        POST /api/items_informacion/
        ```
    
    Notes:
        - Este permiso se utiliza en vistas donde los métodos de lectura son públicos,
          pero los métodos de modificación requieren autenticación.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated


class UniversidadViewSet(viewsets.ModelViewSet):
    """
    UniversidadViewSet
    ------------------
    Vista para manejar el CRUD de universidades.

    Attributes:
        queryset (QuerySet): Conjunto de datos base para las universidades.
        serializer_class (Serializer): Clase de serializador para representar y validar objetos Universidad.
        permission_classes (list): Lista de permisos requeridos, solo usuarios autenticados pueden acceder.

    Methods:
        - list(): Devuelve una lista de todas las instancias de Universidad.
        - create(): Crea una nueva instancia de Universidad.
        - retrieve(): Recupera una instancia específica de Universidad.
        - update(): Actualiza una instancia de Universidad existente.
        - destroy(): Elimina una instancia de Universidad.
        
    Examples:
        ```python
        # Recuperar lista de universidades
        GET /api/universidades/
        
        # Crear una universidad
        POST /api/universidades/
        ```
    
    Notes:
        - La clase utiliza `IsAuthenticated` para asegurar que solo los usuarios autenticados accedan.
    """
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer
    permission_classes = [IsAuthenticated]


class ItemInformacionViewSet(viewsets.ModelViewSet):
    """
    ItemInformacionViewSet
    ----------------------
    Vista para manejar el CRUD de elementos de información asociados a universidades.

    Attributes:
        queryset (QuerySet): Conjunto de datos base para los elementos de información.
        serializer_class (Serializer): Clase de serializador para representar y validar objetos ItemInformacion.
        permission_classes (list): Aplica el permiso `ReadOnlyIfGet`, permitiendo acceso público a métodos seguros.

    Methods:
        - list(): Devuelve una lista de instancias de ItemInformacion, filtrando por universidad si se proporciona el parámetro `universidad`.
        - create(): Crea una nueva instancia de ItemInformacion (requiere autenticación).
        - retrieve(): Recupera una instancia específica de ItemInformacion.
        - update(): Actualiza una instancia existente de ItemInformacion (requiere autenticación).
        - destroy(): Elimina una instancia de ItemInformacion (requiere autenticación).
        - get_queryset(): Filtra los elementos por universidad cuando se proporciona el parámetro `universidad` en la consulta.
        
    Examples:
        ```python
        # Filtrar elementos de información por universidad
        GET /api/items_informacion/?universidad=<id>
        
        # Crear un nuevo elemento de información (requiere autenticación)
        POST /api/items_informacion/
        ```
    
    Notes:
        - `ReadOnlyIfGet` permite acceso público para métodos `GET` y requiere autenticación para los métodos de escritura.
        - Para recuperar solo los elementos de una universidad, añadir el parámetro `universidad` en la URL.
    """
    queryset = ItemInformacion.objects.all()
    serializer_class = ItemInformacionSerializer
    permission_classes = [ReadOnlyIfGet]  # Usa el permiso personalizado

    def get_queryset(self):
        queryset = ItemInformacion.objects.all()
        universidad_id = self.request.query_params.get('universidad', None)
        if universidad_id is not None:
            queryset = queryset.filter(universidad_id=universidad_id)
        return queryset
