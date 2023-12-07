from django.shortcuts import render, HttpResponse

def paginaInicial(request):
    return HttpResponse("Olá, esta é a página inicial.")

def login(request):
    return HttpResponse("Olá, esta é a página de login.")
