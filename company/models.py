from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,auth

# Create your models here.

class com_pro(models.Model):
    #comid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #comid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    com_username=models.CharField(max_length=250)
    com_name = models.CharField(max_length=250)
    com_desc = models.TextField()
    com_place = models.CharField(max_length=250)
    com_pincode =models.BigIntegerField()
    com_dt =models.CharField(max_length=50)
    com_state =models.CharField(max_length=50)
    com_country =models.CharField(max_length=50)
    com_mob =models.BigIntegerField()
    com_email =models.CharField(max_length=250)
    status = models.IntegerField()
    logo = models.FileField(upload_to='media/')
    class meta:
        db_table = "com_pro"

    def __str__(self):
        return self.com_name

class Jobpost(models.Model):
    #comid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #comid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #job_com = models.ForeignKey(com_pro, on_delete = models.CASCADE)
    com_username=models.CharField(max_length=250)
    # com_name = models.CharField(max_length=250)
    job_name = models.CharField(max_length=250)
    job_desc = models.TextField()
    job_qua =models.CharField(max_length=250)
    job_place = models.CharField(max_length=250)
    job_pin =models.IntegerField()
    job_dt =models.CharField(max_length=50)
    job_st =models.CharField(max_length=50)
    job_email =models.CharField(max_length=250)
    job_phn =models.BigIntegerField()
    job_con =models.CharField(max_length=50)
    shrtp_ten =models.FloatField()
    shrtp_tlw =models.FloatField()
    shrtp_ug =models.FloatField()
    shrtp_pg =models.FloatField()
    shrt_skills = models.CharField(max_length=500)
    post_date = models.DateField()
    last_date = models.DateField()
    status =models.IntegerField()

    def __str__(self):
        return self.job_name        


class interview(models.Model):
    job_id = models.IntegerField()
    com_username =models.CharField(max_length=100)
    can_uname =models.CharField(max_length=100)  
    in_desc =models.CharField(max_length=100)
    call = models.CharField(max_length=10)
    call_date = models.DateField()

    def __str__(self):
        return self.com_username


class notification(models.Model):
    job_id = models.IntegerField()
    com_username =models.CharField(max_length=100)
    # com_name = models.CharField(max_length=100)
    # job_name = models.CharField(max_length=100)
    can_uname =models.CharField(max_length=100)  
    in_desc =models.CharField(max_length=100)
    call = models.CharField(max_length=10)
    call_date =models.DateField()
    status = models.IntegerField()

    def __str__(self):
        return self.com_username       

       
    