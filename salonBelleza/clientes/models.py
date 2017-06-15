from django.db import models

# Create your models here.
class Cliente (models.Model):
	cedula=models.IntegerField()
	nombre= models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	correo =models.EmailField()
	def __str__(self): # __unicode__ en Python 2 
	       return '%s %s' % (self.nombre, self.apellido) 
	class Meta: 
		verbose_name_plural = "Clientes"