from django.urls import path
from blog.views import (
    template_hijo,
    template_padre,
    template_inicio,
    template_autor,
    template_articulo,
    template_seccion,
)

urlpatterns = [
    path("inicio/", template_inicio, name="inicio"),
    path("padre/", template_padre, name="padre"),
    path("hijo/", template_hijo, name="hijo"),
    path("autor/", template_autor, name="autor"),
    path("articulo/", template_articulo, name="articulo"),
    path("seccion/", template_seccion, name="seccion"),
]
