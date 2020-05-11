from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth

# Create your models here.

class helpdesk(models.Model):
    username=models.CharField(max_length=100)
   
    message = models.TextField()
   
    help_date =models.DateField()
    
    status =models.IntegerField()
    def __str__(self):
        return self.message
class reply(models.Model):
    help_id =models.IntegerField()  
    message = models.TextField() 
    reply_date =models.DateField()
    status =models.IntegerField()
    def __str__(self):
        return self.message

class payments(models.Model):
    apply_amount = models.FloatField()
    reg_amount = models.FloatField()        

    