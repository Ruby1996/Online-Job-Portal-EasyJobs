from django.shortcuts import render
from django.http import HttpResponse

from company.forms import CompanyForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import com_pro, Jobpost, interview, notification
from candidate.models import can_pro, Jobapply
from administrator.models import helpdesk,reply
from datetime import date
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    cancount = can_pro.objects.filter(status=1).count()
    comcount = com_pro.objects.filter(status=1).count()
    jobcount = Jobpost.objects.filter(status=1).count()
    slt = Jobapply.objects.filter(selected="yes").count()
    
    return render(request, 'com_home.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount,'slt':slt})

def com_about(request):
    cancount = can_pro.objects.filter(status=1).count()
    comcount = com_pro.objects.filter(status=1).count()
    jobcount = Jobpost.objects.filter(status=1).count()
    shrt = Jobapply.objects.filter(short="yes").count()
    slt = Jobapply.objects.filter(selected="yes").count()
    app = Jobapply.objects.all().count()
    return render(request, 'com_about.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount,'slt':slt,'app':app,'shrt':shrt})    

def com_jobs(request, uname):

    jobs = Jobpost.objects.filter(com_username = uname,status=1).order_by('-post_date')
    return render(request, 'com_jobs.html', {'jobs':jobs})    

def com_contact(request):
    return render(request, 'com_contact.html') 

def com_noti(request, uname):
    apply =  Jobpost.objects.filter(com_username = uname,status=1).order_by('-post_date')
    
    return render(request, 'com_noti.html', {'apply':apply})   

def com_viewnoti(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id,status=1)
    # noti = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes",call="yes").order_by('-call_date')
    nc = notification.objects.filter(com_username=uname,job_id=id).count()
    if nc != 0:
        noti = notification.objects.filter(com_username=uname,job_id=id)
        can =[]
        for e in noti:
            cuname = e.can_uname
            canpro=can_pro.objects.get(can_uname=cuname)
            canname = canpro.can_name
            can.append(canname)
        return render(request,'com_viewnoti.html',{'noti':noti,'c':c,'capp':capp,'jname':jname,'can':can})
    else:
        messages.info(request,'No Active Notifications...')
        
        return redirect('com_noti',uname)
 

def com_viewapp(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id,status=1)
    app = Jobapply.objects.filter(com_uname =uname,job_id=id)
    return render(request,'com_viewapp.html',{'app':app,'c':c,'capp':capp,'jname':jname})   


def selection_list(request,uname,id):
   
    slt = Jobapply.objects.filter(com_uname=uname,job_id=id,status=1,selected="yes").count()
    
    jname = Jobpost.objects.get(id=id,status=1)
    jc =  Jobapply.objects.filter(com_uname=uname,job_id=id,selected="yes").count()
    if jc != 0:
        j = Jobapply.objects.filter(com_uname=uname,job_id=id,selected="yes",status=1).order_by('-apply_date')
        can =[]
        for e in j:
            cuname = e.can_uname
            canpro=can_pro.objects.get(can_uname=cuname)
            canname = canpro.can_name
            can.append(canname)
        return render(request,'selection_list.html',{'jname':jname,'slt':slt,'j':j,'can':can})
    else:    
        messages.info(request,'No Active Selection List...')
            
        return redirect('com_accept_applications',id,uname)



def noti_report(request,uname,id):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    rjt = Jobapply.objects.filter(com_uname=uname,job_id=id,status=0).count()
    slt = Jobapply.objects.filter(com_uname=uname,job_id=id,status=1,selected="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id,status=1)
    jc =  Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    if jc != 0:
        j = Jobapply.objects.filter(com_uname=uname,job_id=id).order_by('-apply_date')
        can =[]
        for e in j:
            cuname = e.can_uname
            canpro=can_pro.objects.get(can_uname=cuname)
            canname = canpro.can_name
            can.append(canname)
        return render(request,'noti_report.html',{'j':j,'c':c,'capp':capp,'jname':jname,'rjt':rjt,'slt':slt,'can':can})
    else:    
        messages.info(request,'No Active Report...')
            
        return redirect('com_noti',uname)



def com_editprofile(request, uname):

    compro = com_pro.objects.filter(com_username = uname,status=1)
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
        job = Jobpost(com_username=uname, job_name=jobname, job_desc=dec, job_qua = qua.lower(), job_place=place, job_pin=pin, job_dt=dt, job_st=st, job_email=email, job_phn= phn, job_con=con,shrtp_ten = ten, shrtp_tlw = tlw, shrtp_ug = ug, shrtp_pg = pg, shrt_skills = skills.lower(), post_date = date.today(), last_date=ldate,status=1)

        job.save()
        return render(request, 'com_jobpost.html') 

    else:
        return render(request, 'com_jobpost.html') 


def com_app(request, id,uname):
    c = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,short="yes",selected="no").count()
    if c != 0:
        can = Jobapply.objects.filter(job_id= id,short="yes",status=1,selected="no")
        candidate = []
        for e in can:
            cuname = e.can_uname
            ca = can_pro.objects.get(can_uname=cuname)
            cann = ca.can_name
            candidate.append(cann)
        return render(request, 'com_app.html', {'can':can,'id':id,'candidate':candidate}) 
    else:
        messages.info(request,'No Active Applications...')
        return redirect('com_noti',uname)     


def call_all(request,id,uname):
    c = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,short="yes",selected="no").count()
    if c != 0:
        jobcall = Jobapply.objects.filter(job_id=id,com_uname=uname,status=1,short="yes",selected="no")
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
    job = Jobpost.objects.filter(com_username = comuname,status=1)
    messages.info(request,uname)
    return render(request, 'com_interview.html',{'job':job})


def com_can(request, uname, id, comuname):
    job = Jobpost.objects.get(id = id,status=1)
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

    compro = com_pro.objects.filter(com_username = uname,status=1)
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
        compro = com_pro.objects.get(com_username = uname,status=1)
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
    jobcall = Jobpost.objects.filter(id=id,com_username=uname,status=1)
    return render(request,'call_all1.html',{'jobcall':jobcall})     

def com_jobcall_allnoti(request):
    if request.method == 'POST':
        jobid = request.POST['jid']
        comuname = request.POST['comuname']
        indesc = request.POST['in_desc']
        
        japp = Jobapply.objects.filter(job_id=jobid,com_uname=comuname,short="yes",status=1,selected="no")
        com = com_pro.objects.get(com_username=comuname,status=1)
        job = Jobpost.objects.get(id=jobid,status=1)
        jobname = job.job_name
        comname = com.com_name
        for jap in japp:
             noti = notification(job_id=jobid,com_username=comuname,can_uname=jap.can_uname,in_desc=indesc,call="yes",call_date=date.today(),status=1)
             noti.save()
        return redirect('com_noti', comuname)
    else:
        return render(request, 'com_home.html')        

def com_jobcall_all(request):
    if request.method == 'POST':
        jobid = request.POST['jid']
        comuname = request.POST['comuname']
        indesc = request.POST['in_desc']
        japp = Jobapply.objects.filter(job_id=jobid,selected="no",status=1)
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
        jap = Jobapply.objects.get(job_id=jobid,selected="no",status=1)
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
        job = Jobpost.objects.get(id=jobid,status=1)
        noti = notification(job_id=jobid,com_username=comuname,can_uname=canuname,in_desc=indesc,call="yes",call_date=date.today(),status=1)
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
        return redirect('com_app',jobid,comuname)
   else:
        return render(request, 'com_home.html')           


def com_cannoti(request,uname,id):
    n = notification.objects.filter(job_id=id,can_uname=uname)
    jname = Jobpost.objects.get(id=id,status=1)
    return render(request,'com_cannoti.html',{'n':n,'jname':jname})        


def com_jobcall(request):
   if request.method == 'POST':
        jobid =request.POST['jid']
        indesc = request.POST['in_desc']
        comuname = request.POST['comuname']
        comname =request.POST['comname']
        canuname =request.POST['canuname']
        job = Jobpost.objects.get(id=jobid,status=1)
        
        jap = Jobapply.objects.get(job_id=jobid,can_uname=canuname,com_uname=comuname,comname=comname,call="no",status=1,selected="no")
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
    can=[]
    job=[]
    for e in appl:
        cuname =e.can_uname
        canpro =can_pro.objects.get(can_uname=cuname)
        canname=canpro.can_name
        can.append(canname)

    for e in appl:
        jid = e.job_id
        jobp = Jobpost.objects.get(id=jid,status=1)
        jname =jobp.job_name
        job.append(jname)    
    return render(request,'com_applications.html',{'appl':appl,'can':can,'job':job})

def com_reject_applications1(request,id,uname):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes").count()
    capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
    jname = Jobpost.objects.get(id=id,status=1)
    appl = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,selected="no").order_by('-apply_date')
    can=[]
    for e in appl:
        cuname = e.can_uname
        canpro = can_pro.objects.get(can_uname=cuname)
        canname = canpro.can_name
        can.append(canname)
    return render(request,'com_reject_applications1.html',{'appl':appl,'c':c,'capp':capp,'jname':jname,'can':can})    


def com_reject_applications(request,id,uname):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes",status=1,selected="no").count()
    if c != 0:
        capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
        jname = Jobpost.objects.get(id=id,status=1)
        appl = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,selected="no").order_by('-apply_date')
        can=[]
        for e in appl:
            cuname = e.can_uname
            canpro = can_pro.objects.get(can_uname=cuname)
            canname = canpro.can_name
            can.append(canname)
        return render(request,'com_reject_applications.html',{'appl':appl,'c':c,'capp':capp,'jname':jname,'can':can})
    else:
        
        messages.info(request,'No Active Applications To Reject...')
        
        return redirect('com_noti',uname)     

def com_accept_applications(request,id,uname):
    c = Jobapply.objects.filter(com_uname=uname,job_id=id,short="yes",status=1,selected="no").count()
    if c != 0:
        capp = Jobapply.objects.filter(com_uname=uname,job_id=id).count()
        jname = Jobpost.objects.get(id=id,status=1)
        appl = Jobapply.objects.filter(job_id=id,com_uname = uname,status=1,selected="no").order_by('-apply_date')
        can=[]
        for e in appl:
            cuname = e.can_uname
            canpro = can_pro.objects.get(can_uname=cuname)
            canname = canpro.can_name
            can.append(canname)
        
        return render(request,'com_accept_applications.html',{'appl':appl,'c':c,'capp':capp,'jname':jname,'can':can})
    else:
        
        messages.info(request,'No Active Applications To Select...')
        
        return redirect('com_noti',uname)       


def com_select_can(request,id,uname,comuname):

   
    can = Jobapply.objects.get(job_id=id,can_uname=uname)
    can.selected = "yes"
    can.save()
    return redirect('com_accept_applications',id,comuname) 
    


def com_select_cansearch(request,id,uname,comuname):

    j = Jobapply.objects.get(id=id,can_uname=uname)
    src =Jobapply.objects.get(id=id,can_uname=uname)
    cuname = src.can_uname
    candidate =can_pro.objects.get(can_uname=cuname)
    jid =src.job_id
    post = Jobpost.objects.get(id=jid,status=1)
    if j.selected == "no":
        
        j.selected = "yes"
        j.save()
        src =Jobapply.objects.get(id=id,can_uname=uname)
        return render(request,'com_search_result.html',{'uname':uname,'src':src,'post':post,'candidate':candidate})      
    else:
        messages.info(request,"Already Selected...") 
        return render(request,'com_search_result.html',{'uname':uname,'src':src,'post':post,'candidate':candidate}) 


def com_reject_cansearch(request,id,uname,comuname):
    can = Jobapply.objects.get(id=id,can_uname=uname)
    if can.selected == "yes":
        messages.info(request,'Cannot Reject Selected Candidates...')
        src =Jobapply.objects.get(id=id,can_uname=uname)
        cuname = src.can_uname
        candidate =can_pro.objects.get(can_uname=cuname)
        jid =src.job_id
        post = Jobpost.objects.get(id=jid,status=1)
        return render(request,'com_search_result.html',{'uname':uname,'src':src,'post':post,'candidate':candidate}) 
    else:
        can.status = 0
        can.save()
        messages.info(request,'Successfully Rejected...')
        return redirect('com_search_can',comuname)
    
                            
                 

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


def com_dlt_ac(request):
    return render(request,'com_dlt_ac.html')    


def com_delete(request,uname):
    com = com_pro.objects.get(com_username=uname)
    if request.method == 'POST':
        pass1 = request.POST['pswd']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            
            com.status=0
            com.save()
            auth.logout(request)
            return redirect('/')
            # return render(request,'home.html')
        else:
            messages.info(request,'Invalid Password')
            return redirect('com_dlt_ac')     
    else:
        return redirect('com_dlt_ac')     

def com_search_can(request,uname):
    return render(request,'com_search_can.html',{'uname':uname})    

def com_search_result(request,uname):

    if request.method == 'POST':
        sr =request.POST['sid']
        if sr.isdigit()==True:
        
            if Jobapply.objects.filter(id=sr,com_uname=uname,status=1).exists():
  
                # post=[]
                # candidate=[]
                # for e in src:
                #     jid =e.job_id
                #     j = Jobpost.objects.get(id=jid)
                #     jname =j.job_name
                #     post.append(jname)

                # for e in src:
                #     cuname=e.can_uname
                #     canpro =can_pro.objects.get(can_uname=cuname)
                #     canname =canpro.can_name
                #     candidate.append(canname)    
                src =Jobapply.objects.get(id=sr)
                cuname = src.can_uname
                candidate =can_pro.objects.get(can_uname=cuname)
                jid =src.job_id
                post = Jobpost.objects.get(id=jid,status=1)


                return render(request,'com_search_result.html',{'uname':uname,'src':src,'post':post,'candidate':candidate}) 
            
            else:
                messages.info(request,'No Results...') 
                return render(request,'com_search_can.html',{'uname':uname}) 
        elif sr.isalnum()==True:
            # if can_pro.objects.filter(Q(can_name__icontains=sr)).exists():
            #     src = can_pro.objects.filter(Q(can_name__icontains=sr))
            #     return render(request,'com_search_result.html',{'uname':uname})
            # else:
            messages.info(request,'Invalid Search...') 
            return render(request,'com_search_can.html',{'uname':uname}) 

    else:
        return render(request,'com_search_can.html',{'uname':uname}) 


def reject_view_jobs(request,uname):
    job = Jobpost.objects.filter(com_username = uname,status=1).order_by('-post_date')
    return render(request,'com_reject_jobs.html',{'job':job})

def com_reject_job(request,id,uname):
    job =Jobpost.objects.get(id=id)
    job.status=0
    job.save()
    return redirect('reject_view_jobs',uname)

def com_help(request):
    return render(request,'com_help.html')

def com_help_submit(request,uname):
    if request.method == 'POST':
        msg = request.POST['help']
        h = helpdesk(username = uname,message = msg,help_date=date.today(),status=1)
        h.save()
        return render(request,'com_help.html')  
    else:
        return render(request,'com_help.html')

      
def com_admin_noti(request,uname):
    rply =[]
    date =[]
    rid=[]
    admn = reply.objects.filter(status=1).order_by('-reply_date')
    for e in admn:
        hid = e.help_id
        hlp = helpdesk.objects.get(id=hid)
     
        # cuname = hlp.username
        # c = com_pro.objects.filter(com_username = cuname).count()
        if hlp.username == uname:
            rply.append(e.message)
            date.append(e.reply_date)
            rid.append(e.id)

    return render(request,'com_admin_noti.html',{'rply':rply,'date':date,'rid':rid})    

def com_reject_reply(request,uname,id):
    r = reply.objects.get(id=id)
    r.status=0
    r.save()
    rply =[]
    date =[]
    rid=[]
    admn = reply.objects.filter(status=1).order_by('-reply_date')
    for e in admn:
        hid = e.help_id
        hlp = helpdesk.objects.get(id=hid)
     
        cuname = hlp.username
        c = com_pro.objects.filter(com_username = cuname).count()
        if c != 0:
            rply.append(e.message)
            date.append(e.reply_date)
            rid.append(e.id)

    return render(request,'com_admin_noti.html',{'rply':rply,'date':date,'rid':rid})    



def com_img(request):
    return render(request,'com_img.html')

def com_saveimg(request,uname):
    com = com_pro.objects.get(com_username=uname)
    if request.method == 'POST':    
        res = request.FILES.get('img',False)     
        if res == False:
            pass
        else:
            fs = FileSystemStorage()
            fs.save(res.name,res)
            com.logo = res
            com.save()
        return redirect('com_viewprofile',uname)

def rm_img(request,uname):
     com = com_pro.objects.get(com_username=uname)
     com.logo=""
     com.save()
     return redirect('com_viewprofile',uname)

