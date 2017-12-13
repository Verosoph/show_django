from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'datas':datas})

class Data:                                                 #add
    def __init__(self, name, value, location):              #add
        self.name=name                                      #add
        self.value = value                                  #add
        self.location = location                            #add

datas = [                                                    #add
    Data('one',1,'NM'),                                      #add
    Data('two',2,'CO'),                                      #add
    Data('three',3,'CA')                                    #add
]                                                           #add
