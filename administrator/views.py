from django.shortcuts import render, redirect
from django.http import HttpResponse
from company.models import com_pro, Jobpost, interview, notification
from candidate.models import can_pro, Jobapply
from .models import helpdesk,reply,payments
from datetime import date
import re

from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.http import JsonResponse

from django.views.generic.base import View



# Create your views here.

def home(request):
    return render(request,'admin_home.html')

def admin_company(request):
    com = com_pro.objects.filter(status=1)
    c = com_pro.objects.filter(status=1).count()
    r = com_pro.objects.filter(status=0).count()
    return render(request,'admin_company.html',{'com':com,'c':c,'r':r})

def admin_reject_company(request):
    com = com_pro.objects.filter(status=1)
    rej = com_pro.objects.filter(status=0)
    return render(request,'admin_reject_company.html',{'com':com,'rej':rej})    

def reject_company(request,uname):
    comp = com_pro.objects.get(com_username = uname)
    comp.status = 0 
    comp.save()
    u = User.objects.get(username=uname)
    u.is_active = False
    u.save()
    return redirect('admin_reject_company')



def activate_company(request,uname):
    comp = com_pro.objects.get(com_username = uname)
    comp.status = 1 
    comp.save()
    u = User.objects.get(username=uname)
    u.is_active = True
    u.save()
    return redirect('admin_reject_company')    

def admin_com_jobs(request,uname):
    job = Jobpost.objects.filter(com_username = uname).order_by('-post_date')
    return render(request,'admin_com_jobs.html',{'job':job})

def admin_users(request):
    u = User.objects.filter(is_superuser="False",is_staff="False").order_by('-date_joined')
    return render(request,'admin_users.html',{'u':u})

def admin_candidate(request):
    can = can_pro.objects.filter(status=1)
    c = can_pro.objects.filter(status=1).count()
    r = can_pro.objects.filter(status=0).count()
    return render(request,'admin_candidate.html',{'can':can,'c':c,'r':r})

def admin_reject_candidate(request):
    can = can_pro.objects.filter(status=1)
    rej = can_pro.objects.filter(status=0)
    return render(request,'admin_reject_candidate.html',{'can':can,'rej':rej})    

def reject_candidate(request,uname):
    canp = can_pro.objects.get(can_uname = uname)
    canp.status = 0 
    canp.save()
    u = User.objects.get(username=uname)
    u.is_active = False
    u.save()
    return redirect('admin_reject_candidate') 

def activate_candidate(request,uname):
    canp = can_pro.objects.get(can_uname = uname)
    canp.status = 1
    canp.save()
    u = User.objects.get(username=uname)
    u.is_active = True
    u.save()
    return redirect('admin_reject_candidate')       

def candidate_details(request,uname):
    can = can_pro.objects.get(can_uname = uname)
    return render(request,'candidate_details.html',{'can':can})    


def admin_jobs(request):
    job = Jobpost.objects.filter(status=1).order_by('-post_date')
    c = Jobpost.objects.filter(status=1).count()
    r = Jobpost.objects.filter(status=0).count()
    com =[]
    for e in job:
        cuname = e.com_username
        comp = com_pro.objects.get(com_username = cuname)
        cname = comp.com_name
        com.append(cname)

    return render(request,'admin_jobs.html',{'job':job,'com':com,'c':c,'r':r})

def reject_jobs(request):
    job = Jobpost.objects.filter(status=1).order_by('-post_date')
    com =[]
    for e in job:
        cuname = e.com_username
        comp = com_pro.objects.get(com_username = cuname)
        cname = comp.com_name
        com.append(cname)

    jobr = Jobpost.objects.filter(status=0)
    comr =[]
    for e in jobr:
        cuname = e.com_username
        comp = com_pro.objects.get(com_username = cuname)
        cname = comp.com_name
        comr.append(cname)    
    return render(request,'reject_jobs.html',{'job':job,'com':com,'jobr':jobr,'comr':comr})

def activate_jobs(request,jid):
    job = Jobpost.objects.get(id=jid)
    job.status=1
    job.save()
    return redirect('reject_jobs')    

def delete_jobs(request,jid):
    job = Jobpost.objects.get(id=jid)
    job.status=0
    job.save()
    return redirect('reject_jobs') 


def admin_applications(request):
    app = Jobapply.objects.filter().order_by('-apply_date')
    a = Jobapply.objects.filter(status=1).count()
    s = Jobapply.objects.filter(short="yes").count()
    r = Jobapply.objects.filter(status=0).count()
    sl = Jobapply.objects.filter(status=1,selected="yes").count()

    can =[]
    com =[]
    job = []
    for e in app:
        canuname = e.can_uname
        canpro =can_pro.objects.get(can_uname = canuname)
        canname = canpro.can_name 
        can.append(canname) 
    for e in app:
        comuname = e.com_uname
        compro = com_pro.objects.get(com_username = comuname)
        comname = compro.com_name
        com.append(comname)

    for e in app:
        jid = e.job_id          
        jp = Jobpost.objects.get(id=jid)
        jname =jp.job_name
        job.append(jname)
    return render(request,'admin_applications.html',{'job':job,'com':com,'can':can,'app':app,'a':a,'s':s,'r':r,'sl':sl})


def admin_selection(request):
    app = Jobapply.objects.filter(status=1,selected="yes").order_by('-apply_date')
    sl = Jobapply.objects.filter(status=1,selected="yes").count()
    can =[]
    com =[]
    job = []
    for e in app:
        canuname = e.can_uname
        canpro =can_pro.objects.get(can_uname = canuname)
        canname = canpro.can_name 
        can.append(canname) 
    for e in app:
        comuname = e.com_uname
        compro = com_pro.objects.get(com_username = comuname)
        comname = compro.com_name
        com.append(comname)

    for e in app:
        jid = e.job_id          
        jp = Jobpost.objects.get(id=jid)
        jname =jp.job_name
        job.append(jname)
    return render(request,'admin_selection.html',{'job':job,'com':com,'can':can,'app':app,'sl':sl})



def admin_notifications(request):
    n = notification.objects.filter(status=1).order_by('-call_date')
    post=[]
    com=[]
    can=[]
    for e in n:
        jid = e.job_id
        job = Jobpost.objects.get(id=jid)
        jname = job.job_name
        post.append(jname)
    for e in n:    
        comuname = e.com_username
        compro = com_pro.objects.get(com_username = comuname)
        comname = compro.com_name
        com.append(comname)
    for e in n:
        canuname = e.can_uname
        canpro =can_pro.objects.get(can_uname = canuname)
        canname = canpro.can_name 
        can.append(canname)   
    return render(request,'admin_notifications.html',{'n':n,'com':com,'post':post,'can':can})    

def admin_pswd(request):
    return render(request,'admin_pswd.html')    

def change_password(request):
    if request.method == 'POST':
        
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = 'admin', password = pass1)
        if user is not None:
            u = User.objects.get(username = 'admin')
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Password Changed ,Please Login Again...')
                return render(request,'home.html')
            else:
                messages.info(request,'Password Missmatch...')
                return render(request,'admin_pswd.html') 
           
        else:
            messages.info(request,'Invalid Password...')
            return render(request,'admin_pswd.html') 

    else:
        return render(request,'admin_pswd.html')



def admin_helpdesk(request):

    # com = helpdesk.objects.filter(can_uname = "",status=1).order_by('-help_date')
    # comuser=[]
    # for e in com:
    #     uname = e.com_username
    #     c = com_pro.objects.get(com_username=uname)
    #     cname = c.com_name
    #     comuser.append(cname)
    # can = helpdesk.objects.filter(com_username = "",status=1).order_by('-help_date')
    # canuser=[]
    # for e in can:
    #     uname = e.can_uname
    #     c = can_pro.objects.get(can_uname=uname)
    #     cname = c.can_name
    #     canuser.append(cname)
    hlp = helpdesk.objects.filter(status=1).order_by('-help_date')
    user =[]
    for e in hlp:
        uname = e.username
        c =com_pro.objects.filter(com_username=uname).count()
        if c != 0:
            compro =com_pro.objects.get(com_username = uname)
            comname = compro.com_name
            user.append(comname)
        else:
            canpro = can_pro.objects.get(can_uname=uname)
            canname = canpro.can_name
            user.append(canname)    

    return render(request,'admin_help.html',{'hlp':hlp,'user':user})

def reject_help(request,id):
    n = helpdesk.objects.get(id=id)
    n.status=0
    n.save()    
    return redirect('admin_helpdesk')

def reply_help(request,id):
  return render(request,'reply_help.html',{'id':id})  


def reply_submit(request,id):
    if request.method == 'POST':
        msg = request.POST['reply']  
        r = reply(help_id=id,message=msg,reply_date=date.today(),status=1)
        r.save()
        return render(request,'reply_help.html',{'id':id}) 
    else:
        return render(request,'reply_help.html',{'id':id}) 
       
def pay_amount(request):
    pay = payments.objects.get(id=2)
    return render(request,'admin_payment.html',{'pay':pay}) 

def edit_amount(request):
    if request.method == 'POST':
        ap_am = request.POST['app']
        reg_am = request.POST['reg']
        pay = payments.objects.get(id=2)
        pay.apply_amount = ap_am
        pay.save()
        pay.reg_amount = reg_am
        pay.save()
        pay = payments.objects.get(id=2)
        return render(request,'admin_payment.html',{'pay':pay})

def admin_stati(request):
    com_count = com_pro.objects.filter(status=1).count()
    can_count = can_pro.objects.filter(status=1).count()
    app_count = Jobapply.objects.filter(status=1).count()
    short_count = Jobapply.objects.filter(status=1,short="yes").count()
    sl_count = Jobapply.objects.filter(status=1,selected="yes").count()
    job_count = Jobpost.objects.filter(status=1).count()
    user_count = com_count  + can_count

    comr_count = com_pro.objects.filter(status=0).count()
    canr_count = can_pro.objects.filter(status=0).count()

    return render(request,'admin_stati.html',{'com_count':com_count,'can_count':can_count,'app_count':app_count,
    'short_count':short_count,'sl_count':sl_count,'job_count':job_count,'user_count':user_count,'comr_count':comr_count,'canr_count':canr_count
    })    

# class HomeView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'admin_stati.html',{})

# def get_data(request,*args,**kwargs):
#     data ={
#         "sales":100,
#         "production" :200,
#     }
#     return JsonResponse(data)

