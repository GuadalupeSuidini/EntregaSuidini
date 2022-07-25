from django.shortcuts import render
from usuarios.models import Empleado,Cliente,Proveedor

# Create your views here.



def inicio(request):

    return render(request,"inicio.html")



def empleados(request):

    if request.method == 'POST':
        empleado = Empleado(nombre=request.POST['nombre'],apellido=request.POST['apellido'],fechaNacimiento=request.POST['fechaNacimiento'],email=request.POST['email'],dni=request.POST['dni'])
        empleado.save()
        return render(request,"inicio.html")

    return render(request, "empleados.html")



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
        