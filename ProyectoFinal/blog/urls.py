from django.urls import path
from blog.views import (
    template_hijo,
    template_padre,
    template_inicio,
    template_autor,
    template_articulo,
    template_seccion,
    template_search,
    template_searching,
)

urlpatterns = [
    path("inicio/", template_inicio, name="inicio"),
    path("padre/", template_padre, name="padre"),
    path("hijo/", template_hijo, name="hijo"),
    path("autor/", template_autor, name="autor"),
    path("articulo/", template_articulo, name="articulo"),
    path("seccion/", template_seccion, name="seccion"),
    path("search/", template_search, name="search"),
    path("searching/", template_searching, name="searching"),
]
