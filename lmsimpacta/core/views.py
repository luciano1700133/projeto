from django.shortcuts import render

from core.models import Curso
from core.forms import ContatoForm

def index(request):
    contexto = {
        "usuario":"Pessoinha",
        "perfil":"sbruble",
        "cursos":Curso.objects.all()
    }
    return render(request,"index.html",contexto)

def contato(request):
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()
    
    contexto = {
        "form":form
    }
    return render(request,"contato.html")

def cursos(request):
    return render(request,"cursos.html")

def ads(request):
    return render(request,"ads.html")

def adm(request):
    return render(request,"adm.html")

def enfermagem(request):
    return render(request,"enfermagem.html")

def fisioterapia(request):
    return render(request,"fisioterapia.html")