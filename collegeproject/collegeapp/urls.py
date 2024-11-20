from django.contrib import admin
from django.urls import path,include
from collegeapp import views



urlpatterns =[
    path('adminhome',views.adminhome,name='adminhome'),
    path('mainhome',views.mainhome,name='mainhome'),
    path('',views.index,name='index'),
    path('logins',views.logins,name='logins'),
    path('lgout',views.lgout,name='lgout'),




    path('dep_add',views.dep_add,name='dep_add'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('approve/<int:aid>',views.approve,name='approve'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updateteach',views.updateteach,name='updateteach'),
    path('updateteacher/<int:uid>',views.updateteacher,name='updateteacher'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('approved_teaview',views.approved_teaview,name='approved_teaview'),
    path('deleteteacher/<int:uid>',views.deleteteacher,name='deleteteacher'),
    path('deletestudent/<int:uid>',views.deletestudent,name='deletestudent'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
    path('depbyteacher',views.depbyteacher,name='depbyteacher'),

  

    
   
]