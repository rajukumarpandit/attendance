from django.urls import path
from . import views

urlpatterns = [
    path("qrcodes/",views.qrcodes),
    path("admins/",views.adminDashboard),
    path("adminLoginVeryfy/",views.adminLoginVeryfy),
    path("Admin_register/",views.adminRegister),
    path("Admin_save/",views.saveadmin),
    path("Admin_login/",views.adminLogin),
    path("Timetable/",views.timeTable),
    path("Timetables/",views.saveTimeTable),

    path("teachers/",views.teacherDashboard),
    path("Teacher_login/",views.teacherLogin),
    path("Teacher_register/",views.teacherRegister),
    path("Teacher_registers/",views.teacherRegisters),
    path("teacherLoginVeryfy/",views.teacherLoginVeryfy),

    path("students/",views.studentDashboard),
    path("",views.home),

    path("attendances/",views.attendances),
    path("Student_register/",views.studentRegister),
    path("Student_registers/",views.studentRegisters),
    path("Student_login/",views.studentLogin),
    path("Scanner/",views.scanner),
    path("markattendance/",views.markadttendance),
    path("studentLoginVeryfy/",views.studentLoginVeryfy),


]