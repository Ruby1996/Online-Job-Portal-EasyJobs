from django.shortcuts import render
from django.http import HttpResponse

from company.forms import CompanyForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import com_pro, Jobpost, interview, notification
from candidate.models import can_pro, Jobapply
from datetime import date

# Create your views here.

def home(request):
    cancount = can_pro.objects.all().count()
    comcount = com_pro.objects.all().count()
    jobcount = Jobpost.objects.all().count()
    return render(request, 'com_home.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount})

def com_about(request):
    return render(request, 'com_about.html')    

def com_jobs(request, uname):

    jobs = Jobpost.objects.filter(com_username = uname).order_by('-post_date')
    return render(request, 'com_jobs.html', {'jobs':jobs})    

def com_contact(request):
    return render(request, 'com_contact.html') 

def com_noti(request, uname):
    apply =  Jobpost.objects.filter(com_username = uname).order_by('-post_date')
    
    return render(request, 'com_noti.html', {'apply':apply})   

def com_viewnoti(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id)
    # noti = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes",call="yes").order_by('-call_date')
    nc = notification.objects.filter(com_username=uname,job_id=id).count()
    if nc != 0:
        noti = notification.objects.filter(com_username=uname,job_id=id)
        return render(request,'com_viewnoti.html',{'noti':noti,'c':c,'capp':capp,'jname':jname})
    else:
        messages.info(request,'No Active Notifications...')
        
        return redirect('com_noti',uname)
 

def com_viewapp(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id)
    app = Jobapply.objects.filter(com_uname =uname,job_id=id)
    return render(request,'com_viewapp.html',{'app':app,'c':c,'capp':capp,'jname':jname})    


def noti_report(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    rjt = Jobapply.objects.filter(com_uname=uname,job_id=id,status=0).count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id)
    jc =  Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    if jc != 0:
        j = Jobapply.objects.filter(com_uname=uname,job_id=id).order_by('-apply_date')
        return render(request,'noti_report.html',{'j':j,'c':c,'capp':capp,'jname':jname,'rjt':rjt})
    else:    
        messages.info(request,'No Active Report...')
            
        return redirect('com_noti',uname)



def com_editprofile(request, uname):

    compro = com_pro.objects.filter(com_username = uname)
    return render(request, 'com_editprofile.html', {'compro':compro}) 


def com_jobpost(request, unam):

    #quali = qualification.objects.filter(com_username = unam)
    if request.method == 'POST':
        uname = request.POST['job_hid']
        com_name = request.POST['job_hid2']
        jobname = request.POST['job_name']
        dec = request.POST['job_dec']
        qua = request.POST['job_qua']
        place = request.POST['job_place']
        pin = request.POST['job_pin']
        dt = request.POST['job_dt']
        st = request.POST['job_st']
        email = request.POST['job_email']
        phn = request.POST['job_phn']
        con = request.POST['job_con']
        ten = request.POST['ten']
        tlw = request.POST['tlw']
        ug = request.POST['ug']
        pg = request.POST['pg']
        # skill1 = request.POST['skill1']
        # skill2 = request.POST['skill2']
        # skill3 = request.POST['skill3']
        skills = request.POST['skills']
        ldate = request.POST['ldate']
        
        # job = Jobpost(com_username=uname, com_name=com_name, job_name=jobname, job_desc=dec, job_qua = qua.lower(), job_place=place, job_pin=pin, job_dt=dt, job_st=st, job_email=email, job_phn= phn, job_con=con,shrtp_ten = ten, shrtp_tlw = tlw, shrtp_ug = ug, shrtp_pg = pg, shrt_skill1 = skill1.lower(), shrt_skill2 = skill2.lower(), shrt_skill3 = skill3.lower(), shrt_skills = skills.lower(), post_date = date.today(), last_date=ldate)
        job = Jobpost(com_username=uname, com_name=com_name, job_name=jobname, job_desc=dec, job_qua = qua.lower(), job_place=place, job_pin=pin, job_dt=dt, job_st=st, job_email=email, job_phn= phn, job_con=con,shrtp_ten = ten, shrtp_tlw = tlw, shrtp_ug = ug, shrtp_pg = pg, shrt_skills = skills.lower(), post_date = date.today(), last_date=ldate)

        job.save()
        return render(request, 'com_jobpost.html') 

    else:
        return render(request, 'com_jobpost.html') 


def com_app(request, id,uname):
    c = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,short="yes").count()
    if c != 0:
        can = Jobapply.objects.filter(job_id= id,short="yes",status=1)
        return render(request, 'com_app.html', {'can':can,'id':id}) 
    else:
        messages.info(request,'No Active Applications...')
        return redirect('com_noti',uname)     


def call_all(request,id,uname):
    c = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,short="yes").count()
    if c != 0:
        jobcall = Jobapply.objects.filter(job_id=id,com_uname=uname,status=1,short="yes")
        return render(request,'call_all.html',{'jobcall':jobcall})  
    else:
        messages.info(request,'No Active Applications...')
        return redirect('com_noti',uname)      

def com_interviewnoti(request,canuname,comuname,jobid):
    # if Jobapply.objects.filter(job_id=jobid, can_uname=canuname, com_uname=comuname, call='yes').exists():
    #     messages.info(request,'Already Send...')
    #     return redirect('com_app',jobid)       
    # else:
    jap = Jobapply.objects.filter(job_id=jobid,can_uname=canuname,com_uname=comuname)
    return render(request,'com_interview.html',{'jap':jap})      

def com_interview(request,canuname,comuname,jobid):
    if Jobapply.objects.filter(job_id=jobid, can_uname=canuname, com_uname=comuname, call='yes').exists():
        messages.info(request,'Already Send...')
        return redirect('com_app',jobid)       
    else:
        jap = Jobapply.objects.filter(job_id=jobid,can_uname=canuname,com_uname=comuname)
        return render(request,'com_interview.html',{'jap':jap})  
        


def com_callletter(request, uname, comuname, comname):
    job = Jobpost.objects.filter(com_username = comuname)
    messages.info(request,uname)
    return render(request, 'com_interview.html',{'job':job})


def com_can(request, uname, id, comuname):
    job = Jobpost.objects.get(id = id)
    jname = job.job_name
    if interview.objects.filter(can_uname=uname, job_name=jname, com_username=comuname).exists():
        
        messages.info(request,'Already send...')
        return redirect('com_app', id)
    else:    
        
        canpro = can_pro.objects.filter(can_uname = uname)
        
        #intv = interview(com_username =com_uname, job_name = jname, in_desc ="", com_name = com_name, can_uname =uname)
        #intv.save()
        #return redirect('com_interview',comuname,id, jobname,comname,uname) 
        return render(request, 'com_can.html', {'canpro':canpro}) 

def can_prof(request,canuname):
    canpro = can_pro.objects.filter(can_uname = canuname)
    return render(request, 'com_can.html', {'canpro':canpro})


def com_viewprofile(request, uname):

    compro = com_pro.objects.filter(com_username = uname)
    return render(request, 'com_viewprofile.html', {'compro':compro}) 


def com_saveprofile(request, uname):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        pin = request.POST['pin']
        place = request.POST['place']
        dt = request.POST['dt']
        st = request.POST['st']
        con = request.POST['con']
        mob = request.POST['mob']
        email = request.POST['email']
        compro = com_pro.objects.get(com_username = uname)
        us = User.objects.get(username = uname)  
        us.first_name = name
        us.save()
        compro.com_desc = desc
        compro.save()
        compro.com_pincode = pin
        compro.save()
        compro.com_place = place
        compro.save()
        compro.com_dt = dt
        compro.save()
        compro.com_state = st
        compro.save()
        compro.com_country = con
        compro.save()
        compro.com_mob = mob
        compro.save()
        compro.com_email = email
        compro.save()
        
        return redirect('com_viewprofile', uname)
    else:

        return render(request, 'com_home.html')

def call_all1(request,id,uname):
    jobcall = Jobpost.objects.filter(id=id,com_username=uname)
    return render(request,'call_all1.html',{'jobcall':jobcall})     

def com_jobcall_allnoti(request):
    if request.method == 'POST':
        jobid = request.POST['jid']
        comuname = request.POST['comuname']
        indesc = request.POST['in_desc']
        
        japp = Jobapply.objects.filter(job_id=jobid,com_uname=comuname,short="yes",status=1)
        com = com_pro.objects.get(com_username=comuname)
        job = Jobpost.objects.get(id=jobid)
        jobname = job.job_name
        comname = com.com_name
        for jap in japp:
             noti = notification(job_id=jobid,com_username=comuname,com_name=comname,job_name=jobname,can_uname=jap.can_uname,in_desc=indesc,call="yes",call_date=date.today(),status=1)
             noti.save()
        return redirect('com_noti', comuname)
    else:
        return render(request, 'com_home.html')        

def com_jobcall_all(request):
    if request.method == 'POST':
        jobid = request.POST['jid']
        comuname = request.POST['comuname']
        indesc = request.POST['in_desc']
        japp = Jobapply.objects.filter(job_id=jobid)
        for jap in japp:
            jap.intw_desc = indesc
            jap.save()
            jap.call = "yes"
            jap.save()
            jap.call_date = date.today()
            jap.save()
        return redirect('com_noti', comuname)
    else:
        return render(request, 'com_home.html') 

def com_jobcall_all1(request):
    
    if request.method == 'POST':
        jobid = request.POST['jid']
        comuname =request.POST['comuname']
        indesc = request.POST['in_desc']
        jap = Jobapply.objects.get(job_id=jobid)
        jap.intw_desc = indesc
        jap.save()
        jap.call = "yes"
        jap.save()
        return render(request,'com_noti', comuname)
    else:
        return render(request, 'com_home.html') 

def com_jobcallnoti(request):
   if request.method == 'POST':
        jobid =request.POST['jid']
        indesc = request.POST['in_desc']
        comuname = request.POST['comuname']
        comname =request.POST['comname']
        canuname =request.POST['canuname']
        job = Jobpost.objects.get(id=jobid)
        noti = notification(job_id=jobid,com_username=comuname,com_name=comname,job_name=job.job_name,can_uname=canuname,in_desc=indesc,call="yes",call_date=date.today(),status=1)
        noti.save()
        # jap = Jobapply.objects.get(job_id=jobid,can_uname=canuname,com_uname=comuname,comname=comname,call="no",status=1)
        # if job.post_date <= jap.apply_date and job.last_date >= jap.apply_date:

        #     jap.intw_desc = indesc
        #     jap.save()
        #     jap.call="yes"
        #     jap.save()
        #     jap.call_date = date.today()
        #     jap.save()
        #intv = interview(com_username =comuname, job_name = jobname, in_desc =indesc, com_name = comname, can_uname =canuname)
        #intv.save()
        return redirect('com_app',jobid)
   else:
        return render(request, 'com_home.html')           

        


def com_jobcall(request):
   if request.method == 'POST':
        jobid =request.POST['jid']
        indesc = request.POST['in_desc']
        comuname = request.POST['comuname']
        comname =request.POST['comname']
        canuname =request.POST['canuname']
        job = Jobpost.objects.get(id=jobid)
        
        jap = Jobapply.objects.get(job_id=jobid,can_uname=canuname,com_uname=comuname,comname=comname,call="no",status=1)
        if job.post_date <= jap.apply_date and job.last_date >= jap.apply_date:

            jap.intw_desc = indesc
            jap.save()
            jap.call="yes"
            jap.save()
            jap.call_date = date.today()
            jap.save()
        #intv = interview(com_username =comuname, job_name = jobname, in_desc =indesc, com_name = comname, can_uname =canuname)
        #intv.save()
        return redirect('com_noti', comuname)
   else:
        return render(request, 'com_home.html')   


def com_applications(request, uname):
    appl = Jobapply.objects.filter(com_uname = uname).order_by('-apply_date')
    return render(request,'com_applications.html',{'appl':appl})

def com_reject_applications1(request,id,uname):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id)
    appl = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1).order_by('-apply_date')
    
    return render(request,'com_reject_applications1.html',{'appl':appl,'c':c,'capp':capp,'jname':jname})    


def com_reject_applications(request,id,uname):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes",status=1).count()
    if c != 0:
        capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
        jname = Jobpost.objects.get(id=id)
        appl = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1).order_by('-apply_date')
        
        return render(request,'com_reject_applications.html',{'appl':appl,'c':c,'capp':capp,'jname':jname})
    else:
        
        messages.info(request,'No Active Applications To Reject...')
        
        return redirect('com_noti',uname)     

def com_reject_can(request,id,uname,comuname):
    can = Jobapply.objects.get(job_id=id,can_uname=uname)
    can.status = 0
    can.save()
    notii = notification.objects.filter(job_id=id,can_uname=uname)
    for noti in notii:
        noti.status = 0
        noti.save()
    return redirect('com_reject_applications',id,comuname)   

def com_reject_can1(request,id,uname,comuname):
    can = Jobapply.objects.get(job_id=id,can_uname=uname)
    can.status = 0
    can.save()
    notii = notification.objects.filter(job_id=id,can_uname=uname)
    for noti in notii:
        noti.status = 0
        noti.save()
    return redirect('com_reject_applications1',id,comuname)      

def com_pswd(request,uname):
    return render(request,'com_pswd.html')


def change_password1(request,comuname):
    if request.method == 'POST':
        password1 = request.POST['pswd1']
        password2 = request.POST['pswd2']
        password3 = request.POST['pswd3']
        user = auth.authenticate(username=comuname,password=password1)
        if user is not None:
            if password2 == password3:
                u = User.objects.get(username=comuname)
                u.set_password(password3)
                u.save()
                messages.info(request, 'Successfuly Changed')
                auth.logout(request)
                return redirect('/') 
                #return redirect('login')
            else:
                messages.info(request, 'Password Missmatch')
                return redirect('change_password',comuname)  
        else:
            messages.info(request, 'Invalid User')
            return redirect('change_password',comuname)  
    else:        
        return render(request, 'can_pswd.html',comuname) 

def change_password(request):
    if request.method == 'POST':
        canuname = request.POST['uname']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = canuname, password = pass1)
        if user is not None:
            u = User.objects.get(username = canuname)
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Password Changed ,Please Login Again...')
                return render(request,'home.html')
            else:
                messages.info(request,'Password Missmatch...')
                return redirect('change_password')
           
        else:
            messages.info(request,'Invalid Password...')
            return redirect('change_password')

    else:
        return render(request,'can_pswd.html')

        


