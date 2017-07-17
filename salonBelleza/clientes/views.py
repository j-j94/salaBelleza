from django.shortcuts import render
from clientes.models import Cliente
from django.http import HttpResponse
from django.core.serializers import serialize
from django.http import JsonResponse

# Create your views here.
def clientes(request):
	return render(request, 'bienvenida.html', {'mensaje':'cliente'})

def newCliente(request):
	return render(request, 'addcliente.html')
def verCliente(request):
	return render(request, 'verclientes.html')

def guardarC(request):
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	cl = Cliente(cedula=ce, nombre=n,apellido=a,correo=c)
	cl.save()
	return render(request, 'bienvenida.html', {'mensaje':'cliente guardado'})
def eliminar(request):
	return HttpResponse("algo")
def actualizar(request):
	cli =Cliente.objects.all()
	cli2=serialize('json', cli)
	return HttpResponse(cli2)
