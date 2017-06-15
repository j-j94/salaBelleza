from django.db import models

# Create your models here.

class Producto (models.Model):
	nombre= models.CharField(max_length=50)
	descripcion=models.TextField(blank=True)
	precio =models.IntegerField()
	def __str__(self): # __unicode__ en Python 2 
        	return '%s $%s' %(self.nombre, self.precio)
	class Meta: 
		verbose_name_plural = "Productos" 

class Cliente (models.Model):
	cedula=models.IntegerField()
	nombre= models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	correo =models.EmailField()
	def __str__(self): # __unicode__ en Python 2 
	       return '%s %s' % (self.nombre, self.apellido) 
	class Meta: 
		verbose_name_plural = "Clientes"

class Factura (models.Model):
	fecha= models.DateField()
	idcliente = models.ForeignKey(Cliente)
	productos = models.ManyToManyField(Producto, through='DetFactura')

class DetFactura (models.Model):
	idfactura= models.ForeignKey(Factura)
	idproducto=models.ForeignKey(Producto)
	cantidad =models.IntegerField()
