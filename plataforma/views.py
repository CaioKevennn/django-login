from django.shortcuts import render, redirect

def home(request):
    if request.session.get('login')[0]==True:
        return render (request,"home.html",)
    else:
        return redirect('/auth/login/?status=25')
    