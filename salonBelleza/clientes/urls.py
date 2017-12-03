from django.conf.urls import url, include
from clientes import views


urlpatterns = [
	url(r'^clientes$', views.clientes),
	url(r'^nuevoCliente$', views.newCliente),
	url(r'^guardarCliente$',views.guardarC),
	url(r'^mostrarClientes$',views.verCliente),
	url(r'^actualizar$',views.actualizar),
	url(r'^eliminacion$', views.eliminar),
	url(r'^update$', views.update),
	url(r'^fupdate/(\d+)', views.fupdate)
]
