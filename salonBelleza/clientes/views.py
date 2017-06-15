from django.shortcuts import render
from clientes.models import Cliente

# Create your views here.
def clientes(request):
	return render(request, 'bienvenida.html', {'mensaje':'cliente'})

def newCliente(request):
	return render(request, 'addcliente.html')

def guardarC(request):
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	c = Cliente(cedula=ce, nombre=n,apellido=a,correo=c)
	c.save()
	return render(request, 'bienvenida.html', {'mensaje':'cliente guardado'}) 
