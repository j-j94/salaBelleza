from django.shortcuts import render
from clientes.models import Cliente
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def clientes(request):
	return render(request, 'bienvenida.html', {'mensaje':'cliente'})

def newCliente(request):
	if request.user.is_authenticated():
		return render(request, 'addcliente.html')
	else:
		return HttpResponseRedirect("/invalid")

def verCliente(request):
	if request.user.is_authenticated():
		return render(request, 'verclientes.html')
	else:
		return HttpResponseRedirect("/invalid")

def guardarC(request):
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	cl = Cliente(cedula=ce, nombre=n,apellido=a,correo=c)
	cl.save()
	return render(request, 'bienvenida.html', {'mensaje':'cliente guardado'})
def eliminar(request):
	i= request.POST["id"]
	cli=Cliente.objects.get(pk=i)
	cli.delete();
	return HttpResponse("Eliminado")
def actualizar(request):
	cli =Cliente.objects.all()
	cli2=[]
	for i in cli:
		cli2.append({"nombre":i.nombre+" "+i.apellido, "cedula":i.cedula,
		"correo":i.correo, "boton":"<button id=\""+str(i.pk)+"\" class=\"eliminar\">E</button>"})
	return HttpResponse(json.dumps({"data":cli2}), content_type="aplication/json")
