from django.urls import path

from .import views

urlpatterns = [

    path('', views.home, name='login_home'),  
    path('about/', views.about, name='login_about'),
    path('contact/', views.contact, name='login_contact'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('signup/',views.signup, name='signup'),
    path('com_signup/',views.com_signup, name='com_signup'),
    path('com_home/',views.com_home, name='com_home'),
    path('change_password/<str:canuname>',views.change_password, name='change_password'),
    path('can_home/',views.can_home, name='can_home'),
    path('logout/', views.logout, name='logout')

]