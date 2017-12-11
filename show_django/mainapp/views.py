from django.shortcuts import render

def index(request):
    text = 'Write this text'
    value = 12346
    context = {'mainapp_text':text,'mainapp_value':value}

    return render(request,'index.html',context)

