from django.urls import path

from .import views



urlpatterns = [

    path('home/', views.home, name='admin_home'),
    path('admin_company/',views.admin_company,name='admin_company'),
    path('admin_reject_company/',views.admin_reject_company,name='admin_reject_company'),
    path('reject_company/<str:uname>',views.reject_company,name='reject_company'),
    path('activate_company/<str:uname>',views.activate_company,name='activate_company'),
    path('admin_com_jobs/<str:uname>',views.admin_com_jobs,name="view jobs"),

    path('admin_candidate/',views.admin_candidate,name='admin_candidate'),
    path('candidate_details/<str:uname>',views.candidate_details,name='candidate_details'),
    path('admin_reject_candidate/',views.admin_reject_candidate,name='admin_reject_candidate'),
    path('reject_candidate/<str:uname>',views.reject_candidate,name='reject_candidate'),
    path('activate_candidate/<str:uname>',views.activate_candidate,name='activate_candidate'),

    path('admin_applications/',views.admin_applications,name='admin_applications'),

    path('admin_selection/',views.admin_selection,name='admin_selection'),

    path('admin_users/',views.admin_users,name='admin_users'),

    path('admin_notifications/',views.admin_notifications,name='admin_notifications'),

    path('admin_pswd/',views.admin_pswd,name='admin_pswd'),
    path('change_password/',views.change_password,name='change pswd'),
    
    path('admin_helpdesk/',views.admin_helpdesk,name='help'),
    path('reject_help/<int:id>',views.reject_help,name='reject help'),
    path('reply_help/<int:id>',views.reply_help,name='reply help'),
    path('reply_submit/<int:id>',views.reply_submit,name='reply submit'),

    path('admin_stati/',views.admin_stati,name='statistics'),
    # path('api/data',get_data,name='statistics'),

    path('pay_amount/',views.pay_amount,name="payment"),
    path('edit_amount/',views.edit_amount,name="payment"),

    path('admin_jobs/',views.admin_jobs,name='admin_jobs'),
    path('reject_jobs/',views.reject_jobs,name='reject_jobs'),
    path('delete_jobs/<int:jid>',views.delete_jobs,name='delete_jobs'),
    path('activate_jobs/<int:jid>',views.activate_jobs,name='activate_jobs')
]    