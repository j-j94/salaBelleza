from django.shortcuts import render
from clientes.models import Cliente
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def clientes(request):
	return render(request, 'bienvenida.html', {'mensaje':'cliente'})

def newCliente(request):

		return render(request, 'addcliente.html')


def verCliente(request):
	if request.user.is_authenticated():
		return render(request, 'verclientes.html')
	else:
		return HttpResponseRedirect("/invalid")
def fupdate(request, cid):
	cli=Cliente.objects.get(pk=cid)
	print(id)
	return render(request, 'update.html', {'datos':cli})
def update(request):
	i=request.POST["id"]
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	Cliente.objects.filter(id=i).update(nombre=n)
	Cliente.objects.filter(id=i).update(apellido=a)
	Cliente.objects.filter(id=i).update(cedula=ce)
	Cliente.objects.filter(id=i).update(correo=c)
	return render(request, 'verclientes.html')

def guardarC(request):
	n = request.POST["nombre"]
	a = request.POST["apellido"]
	ce = request.POST["cedula"]
	c = request.POST["correo"]
	cl = Cliente(cedula=ce, nombre=n,apellido=a,correo=c)
	cl.save()
	return render(request, 'principal.html', {'mensaje':'cliente guardado'})
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
		"correo":i.correo, "botonE":"<button id=\""+str(i.pk)+"\" class=\"eliminar btn btn-danger\"><span class=\"glyphicon glyphicon-trash\"></span></button>",
		"botonA":"<button id=\""+str(i.pk)+"\" class=\"act btn btn-success\"><span class=\"glyphicon glyphicon-refresh\"></span></button>"})
	return HttpResponse(json.dumps({"data":cli2}), content_type="aplication/json")
