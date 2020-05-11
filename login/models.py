from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    user_type = models.CharField(max_length=250)
    status = models.IntegerField()

  

    
  
