from django.contrib import admin
from facturacion import models

# Register your models here.
admin.site.register(models.Producto)
admin.site.register(models.Cliente)
admin.site.register(models.Factura)
admin.site.register(models.DetFactura)
