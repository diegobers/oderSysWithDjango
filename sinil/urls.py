from django.contrib import admin
from django.urls import path

from sinil_auth.views import perfil
from pedidos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('pedidos/', index, name='pedidos'),
]
