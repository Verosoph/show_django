from django.contrib import admin                
from django.conf.urls import url, include                #change includes the url.py in the mainapp
#from mainapp import views                                # del - dont need anymore


urlpatterns = [
    url(r'^admin/', admin.site.urls),     
    url(r'^',include('mainapp.urls')),        
 ]
