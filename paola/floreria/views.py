# floreria/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm
from .models import Producto, Contacto

def home(request):
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje en la base de datos
            Contacto.objects.create(
                nombre=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['message']
            )
            
            messages.success(request, 'Formulario enviado correctamente.')
            return redirect('home')
    else:
        form = ContactoForm()
    
    return render(request, 'floreria/menu.html', {'form': form, 'productos': productos})