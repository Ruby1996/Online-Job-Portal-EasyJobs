from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from company.models import com_pro,Jobpost
from candidate.models import can_pro
from django.contrib import messages

from django.contrib import admin
# Create your views here.


def home(request):
    cancount = can_pro.objects.all().count()
    comcount = com_pro.objects.all().count()
    jobcount = Jobpost.objects.all().count()
    return render(request, 'home.html',{'cancount':cancount,'comcount':comcount,'jobcount':jobcount})
  

def about(request):
  
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pswd']
        if can_pro.objects.filter(can_uname = username).exists():
            can = can_pro.objects.get(can_uname = username)
            if can.status == 1:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    
                    if User.objects.filter(last_name="company", username=username).exists():
                        
                    #if auth.authenticate(last_name='company'):    
                        return redirect('com_home') 
                    else:
                        return redirect('can_home')
                else:
                    messages.info(request, 'Invalid username/password')
                    return redirect('login')
            else:
                messages.info(request, 'Please Register')
                return redirect('login')       

        elif com_pro.objects.filter(com_username = username).exists():

            com = com_pro.objects.get(com_username = username)
            if com.status == 1:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    
                    if User.objects.filter(last_name="company", username=username).exists():
                        
                    #if auth.authenticate(last_name='company'):    
                        return redirect('com_home') 
                    else:
                        return redirect('can_home')
                else:
                    messages.info(request, 'Invalid username/password')
                    return redirect('login')
            else:
                messages.info(request, 'Please Register')
                return redirect('login')  

        else:
            return render(request, 'login.html')

    else:
         return render(request, 'login.html')
       

def forgot(request):
    return render(request, 'forgot.html') 

def signup(request):
    
        if request.method == 'POST':
             first_name = request.POST['can_fname']
             last_name = request.POST['can_lname']
             username = request.POST['can_email']
             password1 = request.POST['can_pswd1']
             password2 = request.POST['can_pswd2']
             email = request.POST['can_email']
             name = first_name + " " +last_name
             if(password1 == password2):
                 if User.objects.filter(username=username).exists():
                   messages.info(request,'Username Taken')
                   return redirect('signup') 
                 else:
                   user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                   user.save()
                   can = can_pro(can_uname=username, can_name=name, can_house="", can_place="", can_pincode=0,
                   can_gender="", can_email=email, can_mob=0, can_dt="", can_state="", school ="", sc_board="",
                   sc_percent=0.0, sc_yop=0.0, hss="", hss_board="", hss_stream="", hss_yop=0, hss_percent=0,ug="",ug_uni="",
                   ug_course="", ug_yop=0, ug_percent=0.0, pg="", pg_uni="", pg_course="", pg_yop=0, pg_percent=0,skills="",status=1)
                   can.save()
                   print('user created')
                   messages.info(request, 'Successfully Registered')
                   return redirect('login')
             else:
                   messages.info(request,'Password Missmatch')
                   return redirect('signup')  
        else:
             return render(request, 'signup.html')

def com_signup(request):
     if request.method == 'POST':
             first_name = request.POST['com_name']
            # last_name = request.POST['com_lname']
             username = request.POST['com_email']
             password1 = request.POST['com_pswd1']
             password2 = request.POST['com_pswd2']
             email = request.POST['com_email']

             desc = request.POST['com_desc']
             place = request.POST['com_place']
             pincode = request.POST['com_pincode']
             dt = request.POST['com_dt']
             state = request.POST['com_state']
             country = request.POST['com_country']
             mob = request.POST['com_mob']

             if(password1 == password2):
                 if User.objects.filter(username=username).exists():
                   messages.info(request,'Username Taken')
                   return redirect('com_signup') 
                 else:
                   user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name="company")
                   user.save()
                   com = com_pro(com_username=username, com_name =first_name, com_desc=desc, com_place=place, com_pincode=pincode, com_dt=dt, com_state=state, com_country = country, com_mob =mob, com_email =email,status=1)
                   com.save()
                   
                   print('user created')
                   messages.info(request, 'Successfully Registered')
                   return redirect('login')
             else:
                   messages.info(request,'Password Missmatch')
                   return redirect('com_signup')  
     else:
             return render(request, 'com_signup.html')
        

def com_home(request):
   return render(request, 'com_home.html')    

def can_home(request):
    return render(request, 'can_home.html') 

def change_password(request,canuname):
    if request.method=='POST':
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
                auth.logout(request)
                return redirect('/') 
            else:
                 messages.info(request, 'Password Missmatch')
                 return redirect('change_password',canuname)  
        else:
            messages.info(request, 'Invalid User')
            return redirect('change_password',canuname)  
    else:        
        return render(request, 'can_pswd.html') 
        


        #user = auth.authenticate(username=canuname, password=password1)
        #if user is not None:
            #auth.login(request, user)       
         #   if password2 == password3:
          #      can = User.objects.get(username=canuname)
           #     can.password=password3
            #    can.save()
             #   messages.info(request, 'Successfuly Changed')
              #  return redirect('change_password',canuname)
            #else:
             #   messages.info(request, 'Password Missmatch')
              #  return redirect('change_password',canuname)  
         
    

def logout(request):      
    auth.logout(request)
    return redirect('/')      