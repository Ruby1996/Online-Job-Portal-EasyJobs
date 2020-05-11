from django.urls import path

from . import views

urlpatterns = [
    path('com_pay/',views.CompanyPayment.as_view(),name='CompanyPayment'),
    path('com_charge/', views.com_charge, name='com_charge'),
    path('jobapply_pay/<str:uname>/<str:jobname>/<str:comuname>/<int:id>/<str:canfname>/<str:canlname>', views.HomePageView.as_view(), name='home'),
    # path('jobapply_pay1', views.HomePageView1.as_view(), name='home'),
    path('charge/', views.charge, name='charge'),
    path('home/', views.home, name='can_home'),

    # path('jobapply_pay/<str:uname>/<str:jobname>/<str:comname>/<str:comuname>/<int:id>/<str:canfname>/<str:canlname>', views.jobapply_pay, name='home'),

    path('jobapply_check/<str:uname>/<str:jobname>/<str:comuname>/<int:id>/<str:canfname>/<str:canlname>', views.jobapply_check, name='jobapply')

]