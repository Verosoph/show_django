from django.db import models

# Create your models here.
class Data(models.Model):                           #add
    name = models.CharField(max_length=100)         #add
    value = models.CharField(max_length=100)        #add
    location = models.CharField(max_length=20)      #add
    
    def __str__(self):                              #add
        return self.name                            #add
