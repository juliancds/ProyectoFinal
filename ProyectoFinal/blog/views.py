from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Autor, Articulo, Seccion

# Create your views here.


def template_inicio(request):
    return render(request, "blog/inicio.html")


def template_padre(request):
    return render(request, "blog/padre.html")


def template_hijo(request):
    return render(request, "blog/hijo.html")


def template_autor(request):
    if request.method != "POST":
        return render(request, "blog/autor.html")

    autor = Autor(
        nombre=request.POST["nombre"],
        apellido=request.POST["apellido"],
        profesion=request.POST["profesion"],
    )
    autor.save()
    return render(request, "blog/inicio.html")


def template_articulo(request):
    if request.method != "POST":
        return render(request, "blog/articulo.html")

    articulo = Articulo(
        titulo=request.POST["titulo"],
        texto=request.POST["texto"],
        fecha=request.POST["fecha"],
    )
    articulo.save()
    return render(request, "blog/inicio.html")


def template_seccion(request):
    if request.method != "POST":
        return render(request, "blog/seccion.html")

    seccion = Seccion(nombre=request.POST["nombre"])
    seccion.save()
    return render(request, "blog/inicio.html")


def template_search(request):
    return render(request, "blog/busqueda.html")


def template_searching(request):

    if not request.GET["fecha"]:
        return HttpResponse("<h1>No enviaste datos!</h1>")
    else:
        fecha_a_buscar = request.GET["fecha"]
        fechas = Articulo.objects.filter(fecha=fecha_a_buscar)

        contexto = {"fecha": fecha_a_buscar, "articulos_encontrados": fechas}

        return render(request, "blog/busqueda_resultado.html", contexto)
