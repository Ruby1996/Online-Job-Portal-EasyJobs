from django.urls import path

from .import views

urlpatterns = [

    path('home/', views.home, name='can_home'),
    path('can_about/', views.can_about, name='can_about'),
    path('can_contact/', views.can_contact, name='can_contact'),
    path('can_jobs/<str:uname>', views.can_jobs, name='can_jobs'),
    path('can_noti/<str:uname>', views.can_noti, name='can_noti'),
    path('can_profile/', views.can_profile, name='can_profile'),
    
    path('can_search/', views.can_search, name='can_search'),
    path('can_pswd/', views.can_pswd, name='can_pswd'),
    path('can_about_search/', views.can_about_search, name='can_about_search'),
    path('can_comhome/<str:uname>/<str:canuname>', views.can_comhome, name='can_comhome'),
    path('change_password/',views.change_password, name='change_password'),

    path('jobapply/<str:uname>/<str:jobname>/<str:comname>/<str:comuname>/<int:id>/<str:canfname>/<str:canlname>', views.jobapply, name='jobapply'),
    path('jobsubmit/<str:uname>/<str:jobname>/<str:comuname>/<int:id>', views.jobsubmit, name='jobapply'),
    path('can_viewprofile/<str:uname>', views.can_viewprofile, name='can_viewprofile'),
    path('can_editprofile/<str:uname>', views.can_editprofile, name='can_editprofile'),
    path('can_saveprofile/<str:uname>', views.can_saveprofile, name='can_saveprofile'),
    path('can_app/<str:uname>', views.can_app, name='can_app')
  

  
]