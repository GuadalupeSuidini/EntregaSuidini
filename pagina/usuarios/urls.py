from django.urls import path
from usuarios.views import inicio, clientes, proveedores, empleadosFormularios, clientesFormularios, proveedoresFormularios, busquedaEmpleados, buscar


urlpatterns = [
    path('',inicio, name="inicio"),
    path('Empleados/',empleadosFormularios, name="empleadosFormularios"),
    path('Clientes/',clientesFormularios, name="clientesFormularios"),
    path('Proveedores/',proveedoresFormularios, name="proveedoresFormularios"),
    path('BuscarEmpleados/',busquedaEmpleados, name="busquedaEmpleados"),
    path('Buscar/',buscar, name="buscar"),
]