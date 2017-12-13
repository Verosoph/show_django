from django.shortcuts import render
from .models import Data                                        #add

def index(request):
    datas = Data.objects.all()                                  #add
    return render(request,'index.html',{'datas':datas})


