from typing import ContextManager
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title" : "Página Contato",
        "content" : "Bem-vindo à Página Contato",
        "form" : contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
    #    print(request.POST)
    #    print(request.POST.get("nome_completo"))
    return render(request, "contact/view.html", context)

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("O e-mail deve ser do gmail.com")
        return email