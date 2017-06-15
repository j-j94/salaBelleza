from django.conf.urls import url, include
from facturacion import views

urlpatterns = [    
	url(r'^$', views.bienvenida2),
]
