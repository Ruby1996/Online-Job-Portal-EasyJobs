from django.urls import path

from .import views

urlpatterns = [

    path('home/', views.home, name='com_home'),
    path('com_about/', views.com_about, name='com_about'),
    path('com_contact/', views.com_contact, name='com_contact'),
    path('com_noti/<str:uname>', views.com_noti, name='com_noti'),
    path('com_app/<int:id>/<str:uname>', views.com_app, name='com_app'),
    path('com_can/<str:uname>/<int:id>/<str:comuname>', views.com_can, name='com_can'),
    # path('com_interview/<str:canuname>/<str:comuname>/<int:jobid>', views.com_interview, name='com_interview'),
    path('com_interviewnoti/<str:canuname>/<str:comuname>/<int:jobid>', views.com_interviewnoti, name='com_interviewnoti'),
    path('com_cannoti/<str:uname>/<int:id>',views.com_cannoti,name='com_cannoti'),
    path('com_callletter/<str:uname>/<str:comuname>/<str:comname>', views.com_callletter, name='com_callletter'),
    path('com_editprofile/<str:uname>', views.com_editprofile, name='com_editprofile'),
    path('can_prof/<str:canuname>',views.can_prof,name='can_prof'),
    path('com_pswd/<str:uname>', views.com_pswd, name='com_pswd'),
    path('change_password/', views.change_password, name='change_password'),
    path('com_saveprofile/<str:uname>', views.com_saveprofile, name='com_saveprofile'),
    path('com_viewprofile/<str:uname>', views.com_viewprofile, name='com_viewprofile'),

    path('com_dlt_ac',views.com_dlt_ac,name='com_dlt_ac'),

    path('com_delete/<str:uname>',views.com_delete,name='com_delete'),

    #path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('noti_report/<str:uname>/<int:id>',views.noti_report,name='noti_report'),
    path('com_viewnoti/<str:uname>/<int:id>',views.com_viewnoti,name='com_viewnoti'),
    path('call_all/<int:id>/<str:uname>',views.call_all,name='call_all'),
    # path('com_jobcall/', views.com_jobcall, name='com_jobcall'),
    path('com_jobcallnoti/', views.com_jobcallnoti, name='com_jobcallnoti'),

    # path('com_jobcall_all/', views.com_jobcall_all, name='com_jobcall_all'),
    path('com_jobcall_allnoti/', views.com_jobcall_allnoti, name='com_jobcall_allnoti'),

    path('reject_view_jobs/<str:uname>',views.reject_view_jobs,name="reject jobs"),
    path('com_reject_job/<int:id>/<str:uname>',views.com_reject_job,name="reject jobs"),

    path('com_jobs/<str:uname>', views.com_jobs, name='com_jobs'),
    path('com_applications/<str:uname>', views.com_applications, name='com_applications'),
    path('com_reject_applications/<int:id>/<str:uname>', views.com_reject_applications, name='com_reject_applications'),
    path('com_accept_applications/<int:id>/<str:uname>', views.com_accept_applications, name='com_accept_applications'),

    path('com_reject_applications1/<int:id>/<str:uname>', views.com_reject_applications1, name='com_reject_applications1'),
    path('com_viewapp/<str:uname>/<int:id>',views.com_viewapp,name='com_viewapp'),
    path('com_reject_can/<int:id>/<str:uname>/<str:comuname>',views.com_reject_can,name='com_reject_can'),
    path('com_select_can/<int:id>/<str:uname>/<str:comuname>',views.com_select_can,name='com_select_can'),
    path('com_select_cansearch/<int:id>/<str:uname>/<str:comuname>',views.com_select_cansearch,name='com_select_cansearch'),
    path('com_reject_cansearch/<int:id>/<str:uname>/<str:comuname>',views.com_reject_cansearch,name='com_reject_cansearch'),

    path('selection_list/<int:id>/<str:uname>',views.selection_list,name='selection list'),
    path('com_reject_can1/<int:id>/<str:uname>/<str:comuname>',views.com_reject_can1,name='com_reject_can1'),
    path('com_search_can/<str:uname>',views.com_search_can,name='com_search_can'),
    path('com_search_result/<str:uname>',views.com_search_result,name='com_search_result'),

    path('com_help/',views.com_help,name='com_help'),
    path('com_help_submit/<str:uname>',views.com_help_submit,name='com_help'),

    path('com_admin_noti/<str:uname>',views.com_admin_noti,name='notification_admin'),
    path('com_reject_reply/<str:uname>/<int:id>',views.com_reject_reply,name='reject_admin_noti'),

    path('com_img/',views.com_img,name="photo"),
    path('com_saveimg/<str:uname>',views.com_saveimg,name="photo"),
    path('rm_img/<str:uname>',views.rm_img,name="remove photo"),

    path('com_jobpost/<str:unam>', views.com_jobpost, name='com_jobpost')

  
]