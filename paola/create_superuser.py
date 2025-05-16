import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'el_proyecto.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superusuario creado con éxito.")
else:
    print("El superusuario ya existe.")