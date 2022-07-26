from django.http import HttpResponse
from django.shortcuts import render
from usuarios.models import Empleado,Cliente,Proveedor
from usuarios.forms import EmpleadoFormulario, ClienteFormulario, ProveedorFormulario
# Create your views here.



def inicio(request):

    return render(request,"inicio.html")


def clientes(request):

    if request.method == 'POST':
        cliente = Cliente(nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],dni=request.POST['dni'])
        cliente.save()
        return render(request,"inicio.html")

    return render(request,"clientes.html")



def proveedores(request):

    if request.method == 'POST':
        proveedor = Proveedor(cuit=request.POST['cuit'],razonSocial=request.POST['razonSocial'],email=request.POST['email'])
        proveedor.save()
        return render(request,"inicio.html")

    return render(request,"proveedores.html")



def empleadosFormularios(request):

    if request.method == 'POST':
        miFormulario = EmpleadoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            empleado = Empleado(nombre=data['nombre'],apellido=data['apellido'],fechaNacimiento=data['fechaNacimiento'],email=data['email'],dni=data['dni'])
            empleado.save()
            return render(request,"inicio.html")

    else:
        miFormulario = EmpleadoFormulario()
        
    return render(request, "empleados.html", {'miFormulario': miFormulario}) 



def clientesFormularios(request):

    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],dni=data['dni'])
        cliente.save()
        return render(request,"inicio.html")

    else:
        miFormulario = ClienteFormulario()

    return render(request,"clientes.html", {'miFormulario':miFormulario})



def proveedoresFormularios(request):

    if request.method == 'POST':
        miFormulario = ProveedorFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            proveedor = Proveedor(cuit=data['cuit'],razonSocial=data['razonSocial'],email=data['email'])
            proveedor.save()
            return render(request,"inicio.html")

    else:
        miFormulario = ProveedorFormulario()

    return render(request,"proveedores.html",{'miFormulario':miFormulario})


def busquedaEmpleados(request):

    return render(request,'busquedaEmpleados.html')


def buscar(request):
    
    if request.GET['dni']:
        dni = request.GET['dni']
        empleados = Empleado.objects.filter(dni__icontains=dni)
        return render(request,'resultadoBuscar.html',{'empleados':empleados,'dni':dni})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)