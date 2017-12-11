from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),                 #add localhost:8000/index will show the httpRespons in the def index in views.py
    url(r'^', views.index), 

]