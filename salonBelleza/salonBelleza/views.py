from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect

def bienvenida(request):
	return render(request, 'bienvenida.html',{'mensaje':'Bienvenidos a ECO'})
def principal(request):
		return render(request, 'principal.html')
def invalido(request):
	return render(request, 'bienvenida.html',{'mensaje':'no valido'})
def login(request):
	username = request.POST['usuario']
	password = request.POST['contrasenia']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/principal")
	else:
		# Show an error page
		return HttpResponseRedirect("/invalid")

def logout(request):
	auth.logout(request)
    # Redirect to a success page.
	return HttpResponseRedirect("/")
