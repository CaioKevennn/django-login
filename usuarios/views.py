from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256
def login(request):
    if request.method== "POST":
        return render(request,'login.html')
    elif request.method=='GET':
        return render(request,'login.html',{'status':request.GET.get('status')})

def cadastro(request):
    if request.method == 'POST':
        return render(request,"cadastro.html")
    elif request.method=="GET":
        return render(request,"cadastro.html",{'status':(request.GET.get('status'))})

def valid_cad(request):
    nome=request.POST.get("nome")
    email=request.POST.get("email")
    senha=request.POST.get("senha")
    if len(nome.strip())==0 or len(email.strip())==0:
        return redirect("/auth/cadastro/?status=1")
    if len(senha.strip())<8:
        return redirect('/auth/cadastro/?status=2')
    usuario=Usuario.objects.filter(email=email)
    if len(usuario)>0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha= sha256(senha.encode()).hexdigest()
        usuario=Usuario(nome=nome,
                        senha=senha,
                        email=email)
        usuario.save()
        return redirect("/auth/cadastro/?status=4")
    except:
        return redirect("/auth/cadastro/?status=5")
def valid_log(request):
    email=request.POST.get("email")
    senha=sha256(request.POST.get("senha").encode()).hexdigest()
    usuario=Usuario.objects.filter(email=email).filter(senha=senha)
    if len(usuario)==0:
       return  redirect('/auth/login/?status=0')
    if len(usuario)>0:
        request.session['login']=[True,usuario[0].id]
        return redirect('/plataforma/home')

def sair(request):
    request.session.flash()
    return redirect ('/auth/login')