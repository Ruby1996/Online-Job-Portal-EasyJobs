from django.conf import settings # new
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

from company.forms import CompanyForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from company.models import com_pro, Jobpost, interview, notification
from candidate.models import can_pro, Jobapply
from administrator.models import helpdesk,reply,payments
from datetime import date
import re
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import stripe
from django.template.loader import render_to_string



class CompanyPayment(TemplateView):
    template_name = 'com_pay.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        am = payments.objects.get(id=2)
        
        context['amount'] = am.reg_amount
        return context

def com_charge(request):
    if request.method == 'POST':
        # return render(request, 'com_signup.html')  
        return redirect('com_signup') 
















#######candidate

class HomePageView(TemplateView):
    template_name = 'pay.html'
    
    
        

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        am = payments.objects.get(id=2)
        
        context['amount'] = am.apply_amount
        return context

def charge(request): # new
    # stripe.api_key='sk_test_tYBhTZDOeAPpJ8Nw0qJ1HJ4E00wicBRTC7'
    # if request.method == 'POST':
    #     charge = stripe.Charge.create(
    #         amount=500,
    #         currency='usd',
    #         description='A Django charge',
    #         source=request.POST['stripeToken']
            
    #     )
    if request.method == 'POST':
        jobname = request.POST['job']
        # comname = request.POST['comname1']
        comuname = request.POST['comuname1']
        uname = request.POST['uname1']
        id = request.POST['id1']
        canfname = request.POST['canfname1']
        canlname = request.POST['canlname1']
        canname = canfname + "" + canlname

        flag = 0
        
        canpro = can_pro.objects.get(can_uname = uname,status=1)
        job = Jobapply(job_id =id, com_uname = comuname,can_uname=uname, apply_date = date.today(),short="no",short_date='1111-11-11',status = 0,selected="no")
        job.save()
        shrtjob = Jobpost.objects.get(id=id)
        japply = Jobapply.objects.get(job_id=id, can_uname =uname,com_uname=comuname)
        can = can_pro.objects.get(can_uname = uname,status=1)
        jobp = Jobpost.objects.get(id=id)

        if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
            flag = 1
        # jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"])
        # return render(request, 'can_jobs.html', {'jobs':jobs})

        elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
            flag = 2
            # jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today())
            # return render(request, 'can_jobs.html', {'jobs':jobs})
    
        else:    
            flag = 3
            # jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today())
            
            # return render(request, 'can_jobs.html', {'jobs':jobs})

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

        return render(request, 'charge.html')        

def home(request):
    cancount = can_pro.objects.filter(status=1).count()
    comcount = com_pro.objects.filter(status=1).count()
    jobcount = Jobpost.objects.all().count()
    slt = Jobapply.objects.filter(selected="yes").count()
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

    return render(request, 'can_home.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount,'slt':slt})




def jobapply_check(request, uname, jobname, comuname, id, canfname, canlname):
    flag = 0
    check = 0
    canpro = can_pro.objects.get(can_uname= uname,status=1)
    
    # jobqua = Jobpost.objects.get(com_username = comuname, job_name=jobname)
    canname =canfname + "  " + canlname
    if canpro.can_place=='' or canpro.can_house=='' or canpro.can_pincode==0 or canpro.can_gender=='' or canpro.can_mob==0 or canpro.can_dt=='' or canpro.can_state=='' or canpro.school=='' or canpro.sc_board=='' or canpro.sc_percent==0:
        messages.info(request, 'Please complete your profile...')
        #jobs = Jobpost.objects.filter(id = id)   
        #return render(request,'can_jobs.html',{'jobs':jobs})
        if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
            flag = 1
            jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"],status=1)
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})

        elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
            flag = 2
            jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today(),status=1)
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})
    
        else:    
            flag = 3
            jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today(),status=1)
            
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})

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
            jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"]).order_by('last_date',status=1)
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})

        elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
            flag = 2
            jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today(),status=1).order_by('last_date')
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})
    
        else:    
            flag = 3
            jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12")| Q(job_qua__icontains="any degree") ,last_date__gte= date.today(),status=1).order_by('last_date')
            
            comp =[]
            for e in jobs:
                c = e.com_username
                com =com_pro.objects.get(com_username=c)
                company =com.com_name
                comp.append(company)
            return render(request, 'can_jobs.html', {'jobs':jobs,'comp':comp})

    else:
        # return redirect('jobapply_pay',uname, jobname, comname, comuname, id, canfname, canlname) 
        c = payments.objects.all().count()
        if c != 0:
            am = payments.objects.get(id=2)
            amount =am.apply_amount
        
        
        return render(request,'job_pay.html',{ 'jobname':jobname,'comuname': comuname, 'id':id,'amount':amount})
                    


    
     #############################################################################################    

# class HomePageView1(TemplateView):
#     template_name = 'pay.html'

#     def get_context_data(self, **kwargs): # new
#         context = super().get_context_data(**kwargs)
#         context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#         uname = self.kwargs['uname']
#         jobname = self.kwargs['jobname']
#         comname =self.kwargs['comname']
#         comuname =self.kwargs['comuname']
#         id=self.kwargs['id']
#         canfname=self.kwargs['canfname']
#         canlname=self.kwargs['canlname']

#         canname =canfname + " " + canlname
#         print(canname)
#         flag = 0
#         check = 0
#         canpro = can_pro.objects.get(can_uname= uname,status=1)
    
#         # jobqua = Jobpost.objects.get(com_username = comuname, job_name=jobname)
#         canname =canfname + " " + canlname
#         if canpro.can_place=='' or canpro.can_house=='' or canpro.can_pincode==0 or canpro.can_gender=='' or canpro.can_mob==0 or canpro.can_dt=='' or canpro.can_state=='' or canpro.school=='' or canpro.sc_board=='' or canpro.sc_percent==0:
#             messages.info(self.request, 'Please complete your profile...')
#             #jobs = Jobpost.objects.filter(id = id)   
#             #return render(request,'can_jobs.html',{'jobs':jobs})
#             if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
#                 flag = 1
#                 jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"])
#                 return render(self.request, 'can_jobs.html', {'jobs':jobs})

#             elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
#                 flag = 2
#                 jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today())
#                 return render(self.request, 'can_jobs.html', {'jobs':jobs})
    
#             else:    
#                 flag = 3
#                 jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12") ,last_date__gte= date.today())
                
#                 return render(self.request, 'can_jobs.html', {'jobs':jobs})

#         #elif canpro.can_school == '' or  canpro.hss_stream != jobqua.job_qua or canpro.ug_course != jobqua.job_qua or canpro.pg_course != jobqua.job_qua
#         #   messages.info(request,'Not Eligible for the post')    
#         # return redirect('can_jobs')

#         elif Jobapply.objects.filter(can_uname= uname, job_id = id).exists():
#             messages.info(self.request,'Already Applied')
#             canpro = can_pro.objects.get(can_uname = uname,status=1)
#             #jobs = Jobpost.objects.filter(id = id)   
#             #return render(request,'can_jobs.html',{'jobs':jobs})
#             if canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.ug_course == "" and canpro.pg_course == "" and canpro.hss_stream == "":
#                 flag = 1
#                 jobs = Jobpost.objects.filter(last_date__gte= date.today(), job_qua__in=["10","sslc","tenth","10th"])
#                 # return render(self.request,'can_jobs.html', {'jobs':jobs})
#                 return 

#             elif canpro.school != "" and canpro.sc_board != "" and canpro.sc_percent != "" and canpro.hss_stream != "" and canpro.ug_course == "" and canpro.pg_course == "":
#                 flag = 2
#                 jobs = Jobpost.objects.filter( Q(job_qua__exact= "12") | Q(job_qua__exact= "twelveth") | Q(job_qua__exact= "twelve")| Q(job_qua__icontains= "10") |  Q(job_qua__icontains= "sslc") | Q(job_qua__icontains= "tenth") |  Q(job_qua__icontains= "10th") |  Q(job_qua__icontains= "ten") |   Q(job_qua__icontains= canpro.hss_stream)  , last_date__gte= date.today())
#                 # return render(self.request,'can_jobs.html', {'jobs':jobs})
#                 return 
        
#             else:    
#                 flag = 3
#                 jobs = Jobpost.objects.filter( Q(job_qua__icontains= canpro.pg_course) | Q(job_qua__icontains=canpro.ug_course) | Q(job_qua__icontains= canpro.hss_stream)| Q(job_qua__iexact="12")| Q(job_qua__icontains="any degree") ,last_date__gte= date.today())
                
#                 # return render(self.request,'can_jobs.html', {'jobs':jobs})
#                 return 
    
#         else:   
#             canpro = can_pro.objects.get(can_uname = uname,status=1)
#             job = Jobapply(job_id =id, job_name=jobname,com_uname = comuname, comname =comname,can_uname=uname,canname =canname, apply_date = date.today(),short="no",short_date='1111-11-11',status = 0)
#             job.save()
#             shrtjob = Jobpost.objects.get(id=id)
#             japply = Jobapply.objects.get(job_id=id, can_uname =uname,com_uname=comuname)
#             can = can_pro.objects.get(can_uname = uname,status=1)
#             jobp = Jobpost.objects.get(id=id)
            
        
  
    
#             if flag == 3:
#                 # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.ug_percent >= shrtjob.shrtp_ug and canpro.pg_percent >= shrtjob.shrtp_pg and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
#                 if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.ug_percent >= shrtjob.shrtp_ug and canpro.pg_percent >= shrtjob.shrtp_pg:
#                     if jobp.shrt_skills != "":
#                         sk = can.skills
#                         jk = jobp.shrt_skills
#                         skl = sk
#                         k = jk
#                         rev = re.split(r'[;|,|\s]\s*',skl)
#                         # rev = re.split(r'[,]',skl)
#                         for ch in rev:
                    
#                             if ch in k:
#                                 check = 1
#                                 japply.short="yes"
#                                 japply.save()
#                                 japply.short_date=date.today()
#                                 japply.save()
#                                 japply.status = 1
#                                 japply.save()
#                                 break
#                     else:
#                         japply.short="yes"
#                         japply.save()
#                         japply.short_date=date.today()
#                         japply.save()
#                         japply.status = 1
#                         japply.save()

                    
#                         #shrt = Shortlist(job_id=id,com_uname=comuname,can_uname=uname)
#                         #shrt.save()
                    

#                 canprof = can_pro.objects.filter(can_uname= uname,status=1)
#                 # return render(request, 'can_apply.html',{'canprof':canprof})  
#                 return context
#             elif flag ==2:     
#                 # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
#                 if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.hss_percent >= shrtjob.shrtp_tlw: 
#                     if jobp.shrt_skills != "":
#                         sk = can.skills
#                         jk = jobp.shrt_skills
#                         skl = sk
#                         k = jk
#                         rev = re.split(r'[;|,|\s]\s*',skl)
#                         # rev = re.split(r'[,]',skl)
#                         for ch in rev:
                        
#                             if ch in k:
#                                 check = 1
#                                 japply.short="yes"
#                                 japply.save()
#                                 japply.short_date=date.today()
#                                 japply.save()
#                                 japply.status = 1
#                                 japply.save()
#                                 break
#                     else:
#                         japply.short="yes"
#                         japply.save()
#                         japply.short_date=date.today()
#                         japply.save()
#                         japply.status = 1
#                         japply.save()


#                 canprof = can_pro.objects.filter(can_uname= uname,status=1)
#                 # return render(request, 'can_apply.html',{'canprof':canprof})  
#                 return context
#             else:
#                 # if canpro.sc_percent >= shrtjob.shrtp_ten and canpro.skill1 == shrtjob.shrt_skill1 or canpro.skill2 == shrtjob.shrt_skill2 or canpro.skill3 == shrtjob.shrt_skill3 or canpro.skill1 == shrtjob.shrt_skill2 or canpro.skill1 == shrtjob.shrt_skill3 or canpro.skill2 == shrtjob.shrt_skill3:
#                 if canpro.sc_percent >= shrtjob.shrtp_ten: 
#                     if jobp.shrt_skills != "":
#                         sk = can.skills
#                         jk = jobp.shrt_skills
#                         skl = sk
#                         k = jk
#                         rev = re.split(r'[;|,|\s]\s*',skl)
#                         # rev = re.split(r'[,]',skl)
#                         for ch in rev:
                        
#                             if ch in k:
#                                 check = 1
#                                 japply.short="yes"
#                                 japply.save()
#                                 japply.short_date=date.today()
#                                 japply.save()
#                                 japply.status = 1
#                                 japply.save()
#                                 break
#                     else:
#                         japply.short="yes"
#                         japply.save()
#                         japply.short_date=date.today()
#                         japply.save()
#                         japply.status = 1
#                         japply.save()

                

#                 canprof = can_pro.objects.filter(can_uname= uname,status=1)
#                 # return render(request, 'can_apply.html',{'canprof':canprof}) 
#                 return context


