from django.contrib import admin
from django.urls import path

from sinil_auth.views import perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', perfil, name='profile'),
]
