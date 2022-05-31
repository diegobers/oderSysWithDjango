from django.contrib import admin
from django.urls import path, include

import sinil_auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pedidos/', index, name='pedidos'),

    path("accounts/", include("django.contrib.auth.urls")), 
    path('', sinil_auth.views.perfil, name='perfil'),
    #path('perfil/', sinil_auth.views.perfil, name='perfil'),
]
