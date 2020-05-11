from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth

# Create your models here.

class can_pro(models.Model):

    can_uname = models.CharField(max_length=100)
    can_name = models.CharField(max_length=100)
    can_house = models.CharField(max_length=100)
    can_place = models.CharField(max_length=100)
    can_pincode =models.IntegerField(null=True , blank=True)
    
    can_gender =models.CharField(max_length=50)
    can_email =models.CharField(max_length=250)
    can_mob =models.BigIntegerField(null=True , blank=True)
    can_dt = models.CharField(max_length=100)
    can_state =models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    sc_board = models.CharField(max_length=100)
    sc_percent = models.FloatField(null=True , blank=True)
    sc_yop =models.IntegerField(null=True , blank=True)
    hss = models.CharField(max_length=100)
    hss_board = models.CharField(max_length=100)
    hss_stream = models.CharField(max_length=100)
    hss_yop = models.IntegerField(null=True , blank=True)
    hss_percent = models.FloatField(null=True , blank=True)
    ug = models.CharField(max_length=100)
    ug_uni = models.CharField(max_length=100)
    ug_course = models.CharField(max_length=100)
    ug_yop = models.IntegerField(null=True , blank=True)
    ug_percent = models.FloatField(null=True , blank=True)
    pg = models.CharField(max_length=100)
    pg_uni = models.CharField(max_length=100)
    pg_course = models.CharField(max_length=100)
    pg_yop = models.IntegerField(null=True , blank=True)
    pg_percent = models.FloatField(null=True , blank=True)
    skills = models.CharField(max_length=500)
    resume = models.FileField(upload_to='media/')
    status = models.IntegerField()
    img = models.FileField(upload_to='media/')

    def __str__(self):
        return self.can_name

class Jobapply(models.Model):
    job_id = models.IntegerField()
    # job_name =models.CharField(max_length=100)
    com_uname =models.CharField(max_length=100)
    # comname =models.CharField(max_length=100)
    can_uname = models.CharField(max_length=100)
    # canname =models.CharField(max_length=100)
    apply_date = models.DateField()
    short = models.CharField(max_length=3)
    short_date = models.DateField()  
    status = models.IntegerField()
    selected = models.CharField(max_length=100)
    
    def __str__(self):
        return self.can_uname

      


    