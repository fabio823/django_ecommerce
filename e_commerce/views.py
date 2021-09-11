from typing import ContextManager
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title" : "Página Principal",
        "content" : "Bem-vindo à Página Principal..."
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title" : "Página Sobre",
        "content" : "Bem-vindo à Página Sobre!!!"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    context = {
        "title" : "Página Contato",
        "content" : "Bem-vindo à Página Contato"
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/view.html", context)