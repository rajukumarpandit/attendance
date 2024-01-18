from django.shortcuts import render
from django.http import HttpResponse
from attendance_with_QRcode.models import StudentRegister,Timetable,TeacherRegister,AdminPassword,StudentAttendance
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
import qrcode
from io import BytesIO
from django.core.files import File
import base64
 
def qrcodes(request):
    img = qrcode.make(request.POST.get('Timetableid'))
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode()
    return render(request, 'qrcode.html', {'img_str': img_str})
def markadttendance(request):
    marksave=StudentAttendance(Admission_No=request.GET.get('data'),
                            TimetableID=request.GET.get('data'))
    return  HttpResponse('mark attendance')               
def home(request):
    return render(request,"index.html")

def attendances(request):
    teacher=Timetable.objects.all()
    student=StudentRegister.objects.all()
    #length=len(student)
    return render(request,"attendaces.html",{'tinfo':teacher,'sinfo':student})

# admin dashboard functions.
def adminDashboard(request):
    return render(request,"adminDashboard.html")

def adminLoginVeryfy(request):
    adminid=request.POST.get('adminid')
    password=request.POST.get('password')
    count=AdminPassword.objects.filter(AdminID=adminid, Password=password).count()
    if count>0:
        request.session['is_logged']=True
        teacher=TeacherRegister.objects.all()
        tinfo=Timetable.objects.all()
        ainfo=AdminPassword.objects.all()
        return render(request,"adminDashboard.html",{'info':teacher,'data':tinfo})
        #aid=request.session.get('is_logged')
    else:
        return render(request,"Admin_Login.html")

def adminRegister(request):
    return render(request,"Admin_Register.html")
def saveadmin(request):
    admin=AdminPassword(AdminID=request.POST.get("adminid"),
                        AdminName=request.POST.get("adminname"),
                        Role=request.POST.get("role"),
                        Email_ID=request.POST.get("email"),
                        Password=request.POST.get("password")
                        )
    admin.save()
    return render(request,"Admin_Login.html")
def adminLogin(request):
    return render(request,"Admin_Login.html")

def timeTable(request):
    return render(request,"timetable.html")

def saveTimeTable(request):
    table=Timetable(Faculty_ID_id=request.POST["facultyid"],
                    Course_Name=request.POST["course"],
                    Subject=request.POST["subject"],
                    Room_No=request.POST["roomno"],
                    Date=request.POST["date"],
                    S_Time=request.POST["stime"],
                    E_Time=request.POST["etime"],
                    Day=request.POST["day"])
    table.save()
    return render(request,"adminDashboard.html")

#teacher dashboard function
def teacherDashboard(request):
    return render(request,"teacherDashboard.html")
def teacherLoginVeryfy(request):
    facultyid=request.POST.get('facultyid')
    password=request.POST.get('password')
    count=TeacherRegister.objects.filter(Faculty_ID=facultyid, Password=password).count()
    if count>0:
        request.session['is_logged']=True
        teacher=TeacherRegister.objects.all()
        tinfo=Timetable.objects.all()
        return render(request,"teacherDashboard.html",{'info':teacher,'data':tinfo})
        #aid=request.session.get('is_logged')
    else:
        return render(request,"Teacher_login.html")
def teacherRegister(request):
    return render(request,"teacher_Register.html")
def teacherLogin(request):
    return render(request,"Teacher_Login.html")
def teacherRegisters(request):
    teacher=TeacherRegister(F_Name=request.POST["fname"],
                            M_Name=request.POST["mname"],
                            L_Name=request.POST["lname"],
                            Faculty_ID=request.POST["facultyid"],
                            Email_ID=request.POST["email"],
                            Mobile_NO=request.POST["mobile"],
                            Depatment_Name=request.POST["department"],
                            J_Date=request.POST["jdate"])
    teacher.save()
    return render(request,"adminDashboard.html")


#student dashboard function
def studentDashboard(request):
    return render(request,"studentDashboard.html")
def studentLogin(request):
    return render(request,"Student_login.html")

def studentLoginVeryfy(request):
    admissionid=request.POST.get('admissionno')
    password=request.POST.get('password')
    count=StudentRegister.objects.filter(Admission_No=admissionid, Password=password).count()
    if count>0:
        request.session['is_logged']=True
        #aid=request.session.get('is_logged')
        return render(request,"studentDashboard.html")
    else:
        return render(request,"Student_login.html")
    
def studentRegister(request):
    return render(request,"Student_register.html")

def studentRegisters(request):
    student=StudentRegister(F_Name=request.POST["fname"],
                            M_Name=request.POST["mname"],
                            L_Name=request.POST["lname"],
                            Admission_No=request.POST["admissionNo"],
                            Email_ID=request.POST["email"],
                            Mobile_NO=request.POST["mobile"],
                            Course_Name=request.POST["course"],
                            S_Date=request.POST["sdate"],
                            E_Date=request.POST["edate"])
    student.save()
    return render(request,"adminDashboard.html")

def scanner(request):
    return render(request,"Scanner.html")

