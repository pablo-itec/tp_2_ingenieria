# TP1 - API REST de Biblioteca (Django + DRF)

Práctico integrador: proyecto Django con un modelo, serializers y vistas
funcionales de CRUD implementadas con `@api_view` de Django REST Framework.

## Modelo

`Libro`: título, autor, ISBN, año de publicación, disponibilidad y fecha de
creación.

## Requisitos

- [uv](https://docs.astral.sh/uv/) instalado.

## Instalación y uso

```bash
# Instala Python 3.12 (si hace falta) y las dependencias del proyecto
uv sync

# Aplica las migraciones
uv run python manage.py migrate

# (Opcional) crea un superusuario para usar /admin/
uv run python manage.py createsuperuser

# Levanta el servidor de desarrollo
uv run python manage.py runserver
```

El servidor queda disponible en `http://localhost:8000/`.

## Endpoints

Base: `http://localhost:8000/api/libros/`

| Método | URL                  | Acción                        |
|--------|----------------------|--------------------------------|
| GET    | `/api/libros/`       | Listar todos los libros        |
| POST   | `/api/libros/`       | Crear un libro                 |
| GET    | `/api/libros/<id>/`  | Obtener el detalle de un libro |
| PUT    | `/api/libros/<id>/`  | Actualizar un libro completo   |
| PATCH  | `/api/libros/<id>/`  | Actualizar un libro parcial    |
| DELETE | `/api/libros/<id>/`  | Eliminar un libro              |

### Ejemplo de body para crear/actualizar un libro

```json
{
  "titulo": "Cien años de soledad",
  "autor": "Gabriel García Márquez",
  "isbn": "9780307474728",
  "anio_publicacion": 1967,
  "disponible": true
}
```

Se puede probar la API tanto desde el navegador (Django REST Framework trae
una interfaz navegable) como con un cliente REST (Postman, Bruno,
ThunderClient, etc.).

## Estructura del proyecto

```
config/          # Configuración del proyecto Django (settings, urls)
biblioteca/       # App con el modelo, serializer y vistas de CRUD
manage.py
pyproject.toml    # Dependencias gestionadas con uv
```
