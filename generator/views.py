from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*-'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    length=int(request.GET.get('length',12))
    thepassword=''
    for i in range(length):
        thepassword +=random.choice(characters)
    return render(request,'generator/passwordre.html',{'password':thepassword})
def about(request):
    return render(request,'generator/about.html')
def divya(request):
    return HttpResponse('<h1>Divya </h1> <h2>Prabha karan </h2> <h3>jeevesh</h3>')

