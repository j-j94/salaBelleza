from django.shortcuts import render
from facturacion.models import Factura, DetFactura, Producto
from clientes.models import Cliente



# Create your views here.
def bienvenida2(request):
	return render(request, 'bienvenida.html',{'mensaje':'Bienvenidos a facturacion'})

def newFactura(request):
	cli=Cliente.objects.all();
	pro=Producto.objects.all();
	return render(request, 'newFactura.html',{'cli':cli, 'pro':pro})

def guardarF(request):
	f = request.POST["fecha"]
	idc = request.POST["cliente"]
	cl=Cliente.objects.get(id=idc)
	fa =Factura(fecha=f, idcliente=cl)
	fa.save()
	cant = request.POST["cantidad"]
	idp=request.POST["id"]
	pr=Producto.objects.get(id=idp)
	df= DetFactura(idfactura=fa, idproducto=pr,cantidad=cant)
	df.save()
	return render(request, 'bienvenida.html', {'mensaje':'factura guardada'})
