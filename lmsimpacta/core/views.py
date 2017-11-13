from django.shortcuts import render

from core.models import Curso
from core.forms import ContatoForm, CursoForm

def index(request):
    contexto = {
        "usuario":"Pessoinha",
        "perfil":"sbruble",
        "cursos":Curso.objects.all()
    }
    return render(request,"index.html",contexto)

def curso(request):
    if request.POST:
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CursoForm()
    
    contexto = {
        "form":form
    }
    return render(request,"curso.html",contexto)

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
    return render(request,"contato.html",contexto)

def ads(request):
    return render(request,"ads.html")

def adm(request):
    return render(request,"adm.html")

def enfermagem(request):
    return render(request,"enfermagem.html")

def fisioterapia(request):
    return render(request,"fisioterapia.html")

def noticias(request):
    return render(request,"noticias.html")

def new1(request):
    return render(request,"new1.html")

def institucional(request):
    return render(request,"institucional.html")

def header(request):
    return render(request,"header.html")

def footer(request):
    return render(request,"footer.html")

def esqueceu_a_senha(request):
    return render(request,"esqueceu-a-senha.html")

def detalhe_enf(request):
    return render(request,"detalhe_enf.html")

def detalhe_ads(request):
    return render(request,"detalhe_ads.html")

def detalhe_adm(request):
    return render(request,"detalhe_adm.html")






