import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'el_proyecto.settings')
django.setup()

from floreria.models import Producto

def cargar_datos():
    # Crear productos de ejemplo
    productos = [
        {
            'nombre': 'Ramo de Rosas',
            'descripcion': 'Hermoso ramo de rosas.',
            'precio': 599.99,
        },
        {
            'nombre': 'Ramo de Tulipanes',
            'descripcion': 'Hermoso Ramo de tulipanes.',
            'precio': 499.99,
        },
        {
            'nombre': 'Ramo de Gerberas',
            'descripcion': 'Elegante ramo de Gerberas.',
            'precio': 399.99,
        }
    ]

    # Eliminar productos existentes
    Producto.objects.all().delete()

    # Crear nuevos productos
    for producto_data in productos:
        Producto.objects.create(
            nombre=producto_data['nombre'],
            descripcion=producto_data['descripcion'],
            precio=producto_data['precio'],
        )

    print("Datos de ejemplo cargados con éxito")

if __name__ == "__main__":
    cargar_datos()