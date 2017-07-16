from django.shortcuts import render
from clientes.models import Cliente
from django.http import HttpResponse

# Create your views here.
def clientes(request):
	return render(request, 'bienvenida.html', {'mensaje':'cliente'})

def newCliente(request):
	return render(request, 'addcliente.html')
def verCliente(request):
	cli =Cliente.objects.all()
	return render(request, 'verclientes.html', {'cli':cli})

def guardarC(request):
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	cl = Cliente(cedula=ce, nombre=n,apellido=a,correo=c)
	cl.save()
	return render(request, 'bienvenida.html', {'mensaje':'cliente guardado'})
def eliminar(request):
	p =request.POST["prueba"]
	print(p)
	return HttpResponse("funciono")
