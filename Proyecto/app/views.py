from django.shortcuts import render

from app.models import *

from app.forms import *

# Create your views here.

def lista_consecionarios(request):
    con = Consecionario.objects.all()
    return render(request, "app/lista_consecionarios.html",{'consecionarios':con})

def consecionario_form(request): 
    if request.method == 'POST': 
        form = ConsecionarioForm(request.POST) 

        if form.is_valid():  # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre'] 
            direccion = form.cleaned_data['direccion'] 
            marca = form.cleaned_data['marca'] 

            # Guardar los datos en la base de datos
            consecionario = Consecionario(nombre=nombre, direccion=direccion, marca=marca) 
            consecionario.save()

            # Podrías redirigir o enviar un mensaje de éxito aquí
            return render(request, 'app/consecionario_form.html', {'form': ConsecionarioForm(), 'success': True}) 
        
    else: 
        form = ConsecionarioForm()  # Crear un formulario vacío para el GET

    return render(request, 'app/consecionario_form.html', {'form': form})

def lista_vehiculos(request):
    veh = Vehiculo.objects.all()
    return render(request, "app/lista_vehiculos.html",{'vehiculos':veh})

def vehiculo_form(request): 
    if request.method == 'POST': 
        form = VehiculoForm(request.POST) 

        if form.is_valid():  # Procesar los datos del formulario
            marca = form.cleaned_data['marca'] 
            modelo = form.cleaned_data['modelo'] 
            anio = form.cleaned_data['anio'] 
            patente = form.cleaned_data['patente']
            valor = form.cleaned_data['valor'] 
            kilometraje = form.cleaned_data['kilometraje'] 

            # Guardar los datos en la base de datos
            vehiculo = Vehiculo(marca=marca,modelo=modelo,anio=anio,patente=patente,valor=valor,kilometraje=kilometraje) 
            vehiculo.save()

            # Podrías redirigir o enviar un mensaje de éxito aquí
            return render(request, 'app/vehiculo_form.html', {'form': VehiculoForm(), 'success': True}) 
        
    else: 
        form = VehiculoForm()  # Crear un formulario vacío para el GET

    return render(request, 'app/vehiculo_form.html', {'form': form})

def lista_agentes(request):
    a = Agente.objects.all()
    return render(request, "app/lista_agentes.html",{'agentes':a})

def agente_form(request): 
    if request.method == 'POST': 
        form = AgenteForm(request.POST) 

        if form.is_valid():  # Procesar los datos del formulario
            nombre = form.cleaned_data['nombre'] 
            apellido = form.cleaned_data['apellido'] 
            dni = form.cleaned_data['dni'] 
            edad = form.cleaned_data['edad']
            sueldo = form.cleaned_data['sueldo'] 

            # Guardar los datos en la base de datos
            agente = Agente(nombre=nombre,apellido=apellido,dni=dni,edad=edad,sueldo=sueldo) 
            agente.save()

            # Podrías redirigir o enviar un mensaje de éxito aquí
            return render(request, 'app/agente_form.html', {'form': AgenteForm(), 'success': True}) 
        
    else: 
        form = AgenteForm()  # Crear un formulario vacío para el GET

    return render(request, 'app/agente_form.html', {'form': form})

def buscar_agentes(request):
    form = AgenteBusqueda(request.POST) 
    buscar = None   
    
    if request.method == 'POST': 
        if form.is_valid():
            dni = form.cleaned_data['dni'] 
            buscar = Agente.objects.all()
            buscar = buscar.filter(dni=dni)

    return render(request, 'app/buscar_agentes.html', {'form': form, 'resultados': buscar})
