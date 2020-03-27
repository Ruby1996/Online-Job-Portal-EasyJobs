from django.shortcuts import render
from django.http import HttpResponse

from company.forms import CompanyForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from company.models import com_pro, Jobpost, interview, notification
from candidate.models import can_pro, Jobapply
from datetime import date
import re
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    cancount = can_pro.objects.filter(status=1).count()
    comcount = com_pro.objects.filter(status=1).count()
    jobcount = Jobpost.objects.all().count()
    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
            #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp})    

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')
        else:
            return render(request,'can_home.html')        

    return render(request, 'can_home.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount})

def can_about(request):
    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
            #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp}) 

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html') 
        else:
            return render(request,'can_about.html')          

    return render(request, 'can_about.html')    

def can_jobs(request, uname):
    canpro = can_pro.objects.get(can_uname= uname,status=1)
    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
        #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp})

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html') 
        else:
            return redirect('can_jobs',uname)        
    #jobs = Jobpost.objects.filter(last_date__gte= date.today())    
    #jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=[canpro.pg_course,canpro.ug_course, job])
    
    if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
        jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"]).order_by('-post_date')
        return render(request, 'can_jobs.html', {'jobs':jobs})

    elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
        jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today()).order_by('-post_date')
        return render(request, 'can_jobs.html', {'jobs':jobs})

    elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course != "" and canpro.pg_course == "":
        jobs = Jobpost.objects.filter(Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today()).order_by('-post_date')

        return render(request, 'can_jobs.html', {'jobs':jobs})
 
    else:    
    
        jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today()).order_by('-post_date')
        
        return render(request, 'can_jobs.html', {'jobs':jobs})
    
       
       

def can_contact(request):
    return render(request, 'can_contact.html') 

def can_notireject(request,uname,id):
    n = notification.objects.get(id=id,can_uname=uname)
    n.status = 0
    n.save()
    # for e in n:
    #     n.status = 0
    #     n.save()
    return redirect('can_noti',uname)    

def can_noti(request, uname):
    #intrv = interview.objects.filter(can_uname = uname)
    # intrv = Jobapply.objects.filter(can_uname = uname,call="yes",short="yes").order_by('-call_date')
    
    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
        #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp})
   

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html') 
        else:
            return redirect('can_noti', uname)     
    intrv = notification.objects.filter(can_uname = uname,call ="yes",status=1).order_by('-call_date') 
    
         
    return render(request, 'can_noti.html', {'intrv':intrv})   

def can_profile(request):
    return render(request, 'can_profile.html')      

def can_app(request, uname):
    jobs = Jobapply.objects.filter(can_uname = uname).order_by('-apply_date')
    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
        #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp})  

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')  
        return redirect('can_app', uname)        
    return render(request, 'can_app.html',{'jobs':jobs})     



def can_viewprofile(request, uname):
    canpro = can_pro.objects.filter(can_uname= uname,status=1)

    if request.method == 'POST': 
        srch = request.POST['srch']
        loc = request.POST['loc']

        if srch != "" and loc != "":
        #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})

           
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

        elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

        elif srch == "" and loc != "":
            if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

                comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
                return render(request,'can_search.html',{'comp':comp})     

            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   
        else:
            return redirect('can_viewprofile',uname)        
    return render(request, 'can_viewprofile.html',{'canpro':canpro})  
    

def jobapply(request, uname, jobname, comname, comuname, id, canfname, canlname):
    flag = 0
    check = 0
    canpro = can_pro.objects.get(can_uname= uname,status=1)
    
    # jobqua = Jobpost.objects.get(com_username = comuname, job_name=jobname)
    canname =canfname + " " + canlname
    if canpro.can_place=='' or canpro.can_house=='' or canpro.can_pincode==0 or canpro.can_gender=='' or canpro.can_mob==0 or canpro.can_dt=='' or canpro.can_state=='' or canpro.school=='' or canpro.sc_board=='' or canpro.sc_percent==0:
        messages.info(request, 'Please complete your profile...')
        #jobs = Jobpost.objects.filter(id = id)   
        #return render(request,'can_jobs.html',{'jobs':jobs})
        if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
            flag = 1
            jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"])
            return render(request, 'can_jobs.html', {'jobs':jobs})

        elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
            flag = 2
            jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today())
            return render(request, 'can_jobs.html', {'jobs':jobs})
    
        else:    
            flag = 3
            jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today())
            
            return render(request, 'can_jobs.html', {'jobs':jobs})

    #elif canpro.can_school == '' or  canpro.hss_stream != jobqua.job_qua or canpro.ug_course != jobqua.job_qua or canpro.pg_course != jobqua.job_qua
     #   messages.info(request,'Not Eligible for the post')    
       # return redirect('can_jobs')

    elif Jobapply.objects.filter(can_uname= uname, job_id = id).exists():
        messages.info(request,'Already Applied') 
        canpro = can_pro.objects.get(can_uname = uname,status=1)
        #jobs = Jobpost.objects.filter(id = id)   
        #return render(request,'can_jobs.html',{'jobs':jobs})
        if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
            flag = 1
            jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"])
            return render(request, 'can_jobs.html', {'jobs':jobs})

        elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
            flag = 2
            jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today())
            return render(request, 'can_jobs.html', {'jobs':jobs})
    
        else:    
            flag = 3
            jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12")| Q(job_qua__icontains="any degree") ,last_date__gte= date.today())
            
            return render(request, 'can_jobs.html', {'jobs':jobs})
    
    else:   
        canpro = can_pro.objects.get(can_uname = uname,status=1)
        job = Jobapply(job_id =id, job_name=jobname,com_uname = comuname, comname =comname,can_uname=uname,canname =canname, apply_date = date.today(),short="no",short_date='1111-11-11',status = 0)
        job.save()
        shrtjob = Jobpost.objects.get(id=id)
        japply = Jobapply.objects.get(job_id=id, can_uname =uname,com_uname=comuname)
        can = can_pro.objects.get(can_uname = uname,status=1)
        jobp = Jobpost.objects.get(id=id)
        
        
  
    
        if flag == 3:
            # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.ug_percent >= shrtjob.shrtp_ug and canpro.pg_percent >= shrtjob.shrtp_pg and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
            if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.ug_percent >= shrtjob.shrtp_ug and canpro.pg_percent >= shrtjob.shrtp_pg:
                if jobp.shrt_skills != "":
                    sk = can.skills
                    jk = jobp.shrt_skills
                    skl = sk
                    k = jk
                    rev = re.split(r'[;|,|\s]\s*',skl)
                    # rev = re.split(r'[,]',skl)
                    for ch in rev:
                    
                        if ch in k:
                            check = 1
                            japply.short="yes"
                            japply.save()
                            japply.short_date=date.today()
                            japply.save()
                            japply.status = 1
                            japply.save()
                            break
                else:
                    japply.short="yes"
                    japply.save()
                    japply.short_date=date.today()
                    japply.save()
                    japply.status = 1
                    japply.save()

                    
                    #shrt = Shortlist(job_id=id,com_uname=comuname,can_uname=uname)
                    #shrt.save()
                

            canprof = can_pro.objects.filter(can_uname= uname,status=1)
            return render(request, 'can_apply.html',{'canprof':canprof})  
        elif flag ==2:     
            # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
            if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw: 
                if jobp.shrt_skills != "":
                    sk = can.skills
                    jk = jobp.shrt_skills
                    skl = sk
                    k = jk
                    rev = re.split(r'[;|,|\s]\s*',skl)
                    # rev = re.split(r'[,]',skl)
                    for ch in rev:
                    
                        if ch in k:
                            check = 1
                            japply.short="yes"
                            japply.save()
                            japply.short_date=date.today()
                            japply.save()
                            japply.status = 1
                            japply.save()
                            break
                else:
                    japply.short="yes"
                    japply.save()
                    japply.short_date=date.today()
                    japply.save()
                    japply.status = 1
                    japply.save()


            canprof = can_pro.objects.filter(can_uname= uname,status=1)
            return render(request, 'can_apply.html',{'canprof':canprof})  
        else:
            # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
            if canpro.sc_percent >= shrtjob.shrtp_ten: 
                if jobp.shrt_skills != "":
                    sk = can.skills
                    jk = jobp.shrt_skills
                    skl = sk
                    k = jk
                    rev = re.split(r'[;|,|\s]\s*',skl)
                    # rev = re.split(r'[,]',skl)
                    for ch in rev:
                    
                        if ch in k:
                            check = 1
                            japply.short="yes"
                            japply.save()
                            japply.short_date=date.today()
                            japply.save()
                            japply.status = 1
                            japply.save()
                            break
                else:
                    japply.short="yes"
                    japply.save()
                    japply.short_date=date.today()
                    japply.save()
                    japply.status = 1
                    japply.save()

                

            canprof = can_pro.objects.filter(can_uname= uname,status=1)
            return render(request, 'can_apply.html',{'canprof':canprof}) 


def jobsubmit(request, uname, jobname, comuname, id):
    job = Jobapply(job_id =id, job_name=jobname,com_uname =comuname,can_uname=uname)
    job.save()
    return render(request, 'can_jobs.html')         

def can_editprofile(request, uname):
    canpro = can_pro.objects.filter(can_uname= uname,status=1)
    return render(request, 'can_editprofile.html',{'canpro':canpro})    

def can_saveprofile(request, uname):

    
    if request.method == 'POST':
        name = request.POST['can_name']
        house = request.POST['can_house']
        pin = request.POST['can_pin']
        place = request.POST['can_place']
        dt = request.POST['can_dt']
        st = request.POST['can_st']
        gender = request.POST['gender']
        mob = request.POST['can_phn']
        email = request.POST['can_email']
        sc = request.POST['can_sc']
        scb = request.POST['can_scb']
        scp = request.POST['can_scp']
        if scp == "":
            scp =0.0
        scyop = request.POST['can_scyop']
        if scyop == "":
            scyop=0
        hss = request.POST['can_hss']
        hssb = request.POST['can_hssb']
        hsss = request.POST['can_hsss']
        hssp = request.POST['can_hssp']
        if hssp == "":
            hssp =0.0
        hssyop = request.POST['can_hssyop']
        if hssyop == "":
            hssyop=0
        ug =  request.POST['can_ug']
        uguni = request.POST['can_uguni']
        ugc =  request.POST['can_ugc']
        ugp =  request.POST['can_ugp']
        if ugp == "":
            ugp =0.0
        ugyop =   request.POST['can_ugyop']
        if ugyop == "":
            ugyop=0
        pg =   request.POST['can_pg']
        pguni =   request.POST['can_pguni']
        pgc =  request.POST['can_pgc']
        pgp =  request.POST['can_pgp']
        if pgp == "":
            pgp =0.0
        pgyop =  request.POST['can_pgyop']
        if pgyop == "":
            pgyop=0
        # skill1 = request.POST['skill1']
        # skill2 = request.POST['skill2']
        # skill3 = request.POST['skill3']
        skills = request.POST['skills']
        canpro = can_pro.objects.get(can_uname = uname,status=1)
        res = request.FILES['resume'] 
        if res == False:
            res = canpro.resume
            
        else:
            fs = FileSystemStorage()
            fs.save(res.name,res)
          

        
        #us = User.objects.get(username = uname)  
        #us.first_name = name
        #us.save()

        canpro.can_name = name
        canpro.save()
        canpro.can_house = house
        canpro.save()
        canpro.can_place = place
        canpro.save()
        canpro.can_pincode = pin
        canpro.save()
        canpro.can_gender = gender
        canpro.save()
        canpro.can_email = email
        canpro.save()
        canpro.can_mob = mob
        canpro.save()
        canpro.can_dt = dt
        canpro.save()
        canpro.can_state = st
        canpro.save()
        canpro.school = sc
        canpro.save()
        canpro.sc_board = scb
        canpro.save()
        canpro.sc_percent = scp
        canpro.save()
        canpro.sc_yop = scyop
        canpro.save()
        canpro.hss = hss
        canpro.save()
        canpro.hss_board = hssb
        canpro.save()
        canpro.hss_stream = hsss
        canpro.save()
        canpro.hss_yop = hssyop
        canpro.save()
        canpro.hss_percent = hssp
        canpro.save()
        canpro.ug = ug
        canpro.save()
        canpro.ug_uni = uguni
        canpro.save()
        canpro.ug_course = ugc.lower()
        canpro.save()
        canpro.ug_yop = ugyop
        canpro.save()
        canpro.ug_percent = ugp
        canpro.save()
        canpro.pg = pg
        canpro.save()
        canpro.pg_uni = pguni
        canpro.save()
        canpro.pg_course = pgc.lower()
        canpro.save()
        canpro.pg_yop = pgyop
        canpro.save()
        canpro.pg_percent = pgp
        canpro.save()
        # canpro.skill1 = skill1.lower()
        # canpro.save()
        # canpro.skill2 = skill2.lower()
        # canpro.save()
        # canpro.skill3 = skill3.lower()
        # canpro.save()
        canpro.skills = skills.lower()
        canpro.save()
       
        canpro.resume = res
        canpro.save()
       
        return redirect('can_viewprofile', uname)
    else:

        return render(request, 'can_home.html')

def can_search(request):

 if request.method == 'POST': 
    srch = request.POST['srch']
    loc = request.POST['loc']

    if srch != "" and loc != "":
        #comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc))
            if com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():
                comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)

                return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')

    elif srch != "" and loc == "":
            if com_pro.objects.filter(Q(com_name__icontains=srch),status=1).exists():

               comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
               return render(request,'can_search.html',{'comp':comp})
            else:
                messages.info(request, 'No Results...')
                return render(request,'can_search.html')   

    elif srch == "" and loc != "":
        if com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1).exists():

            comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
            return render(request,'can_search.html',{'comp':comp})   

        else:
            messages.info(request, 'No Results...')
            return render(request,'can_search.html')
    else:
        return render(request,'can_home.html')            

def can_about_search(request):

 if request.method == 'POST': 
    srch = request.POST['srch']
    loc = request.POST['loc']

    if srch != "" and loc != "":
        comp = com_pro.objects.filter(Q(com_name__icontains=srch)|Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
        return render(request,'can_search.html',{'comp':comp})

    elif srch != "" and loc == "":
        comp = com_pro.objects.filter(Q(com_name__icontains=srch),status=1)
        return render(request,'can_search.html',{'comp':comp})

    elif srch == "" and loc != "":
        comp = com_pro.objects.filter(Q(com_place__icontains=loc)|Q(com_dt__icontains=loc)|Q(com_state__icontains=loc)|Q(com_country__icontains=loc),status=1)
        return render(request,'can_search.html',{'comp':comp})    

    else:
        return render(request,'can_about.html')   


def can_comhome(request,uname,canuname):
    com = com_pro.objects.filter(com_username = uname,status=1)
    canpro = can_pro.objects.get(can_uname=canuname,status=1)

    if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
        jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"],com_username=uname)
        return render(request, 'can_jobs.html', {'jobs':jobs})

    elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
        jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today(),com_username=uname)
        return render(request, 'can_jobs.html', {'jobs':jobs})
 
    else:    
    
        jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today(),com_username=uname)
        
        return render(request, 'can_jobs.html', {'jobs':jobs})
    
    return render(request,'can_search.html',uname,canuname) 



def can_pswd(request):
       return render(request,'can_pswd.html') 

def change_password1(request,canuname):
    if request.method == 'POST':
        password1 = request.POST['pswd1']
        password2 = request.POST['pswd2']
        password3 = request.POST['pswd3']
        user = auth.authenticate(username=canuname,password=password1)
        if user is not None:
            if password2 == password3:
                u = User.objects.get(username=canuname)
                u.set_password(password3)
                u.save()
                messages.info(request, 'Successfuly Changed')
                 
                return redirect('/') 
                #return redirect('login')
            else:
                 messages.info(request, 'Password Missmatch')
                 return redirect('change_password',canuname)  
        else:
            messages.info(request, 'Invalid Password')
            return redirect('change_password',canuname)  
    else:        
        return render(request, 'can_pswd.html') 
 

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

def can_dlt_ac(request):
    return render(request,'can_dlt_ac.html')

def can_delete(request,uname):
    can = can_pro.objects.get(can_uname=uname)
    if request.method == 'POST':
        pass1 = request.POST['pswd']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            
            can.status=0
            can.save()
            auth.logout(request)
            return redirect('/')
            # return render(request,'home.html')
        else:
            messages.info(request,'Invalid Password')
            return redirect('can_dlt_ac')     
    else:
        return redirect('can_dlt_ac')     


def resume(request,res):
    f = request.FILES.open(res)
    



