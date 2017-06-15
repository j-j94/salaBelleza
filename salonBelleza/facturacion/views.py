from django.shortcuts import render



# Create your views here.
def bienvenida2(request):
	return render(request, 'bienvenida.html',{'mensaje':'Bienvenidos a facturacion'})

