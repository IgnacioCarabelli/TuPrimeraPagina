
from django.urls import path
from . import views


urlpatterns = [
    path("inicio/", views.inicio, name="Inicio"),
    path("cargadeadmin/", views.adminForm, name = "cargadeadmin"),
    path("cargadeusuarios/", views.usuarioForm, name = "cargadeusuarios"),
    path("publicaciones/", views.publicaciones, name = "publicaciones"),
    path("listado_de_admin/", views.listadoDeAdministradores, name = "listado_de_admin"),
]
