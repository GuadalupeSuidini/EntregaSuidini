from django.contrib import admin

from .models import Cliente, Empleado, Proveedor

# Register your models here.


admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proveedor)