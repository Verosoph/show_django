from django.shortcuts import render
from django.http import HttpResponse    #add 

# Create your views here.
def index(request):                                     #add
    return HttpResponse('<h1>Hello World!</h1>')        #add

def marmet(request):
    return HttpResponse('<h1>funzzt</h1>')        #add
    
