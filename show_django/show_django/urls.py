from django.contrib import admin
from django.urls import path                    
from django.conf.urls import url                #add
from mainapp import views                       #add


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/', views.index),               #add
    url(r'^marmet/', views.marmet),               #add
    
]
