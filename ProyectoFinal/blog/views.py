from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def template_padre(request):
    return render(request, "blog/padre.html")


def template_hijo(request):
    return render(request, "blog/hijo.html")
