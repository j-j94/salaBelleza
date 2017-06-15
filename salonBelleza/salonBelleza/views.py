from django.shortcuts import render

def bienvenida(request):
	return render(request, 'bienvenida.html',{'mensaje':'Bienvenidos a ECO'})

