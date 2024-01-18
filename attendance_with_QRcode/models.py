from django.db import models

# Create your models here.

class StudentRegister(models.Model):
    F_Name=models.CharField(max_length=20)
    M_Name=models.CharField(max_length=20)
    L_Name=models.CharField(max_length=20)
    Admission_No=models.IntegerField(primary_key=True) 
    Email_ID=models.CharField(max_length=50,unique=True)
    Mobile_NO=models.IntegerField()
    Course_Name=models.CharField(max_length=20)
    S_Date=models.DateField()
    E_Date=models.DateField()
    Password=models.CharField(max_length=50)

class TeacherRegister(models.Model):
    F_Name=models.CharField(max_length=20)
    M_Name=models.CharField(max_length=20)
    L_Name=models.CharField(max_length=20)
    Faculty_ID=models.IntegerField(primary_key=True)
    Email_ID=models.CharField(max_length=50,unique=True)
    Mobile_NO=models.IntegerField(unique=True)
    Depatment_Name=models.CharField(max_length=20)
    J_Date=models.DateField()
    Password=models.CharField(max_length=50)

class Timetable(models.Model):
    TimetableID=models.AutoField(primary_key=True)
    Faculty_ID=models.ForeignKey(TeacherRegister,on_delete=models.CASCADE)
    Course_Name=models.CharField(max_length=20)
    Subject=models.CharField(max_length=20)
    Room_No=models.IntegerField()
    Date=models.DateField()
    S_Time=models.TimeField()
    E_Time=models.TimeField()
    Day=models.CharField(max_length=10)
    
class StudentAttendance(models.Model):
    Admission_No=models.ForeignKey(StudentRegister,on_delete=models.CASCADE)
    TimetableID=models.ForeignKey(Timetable,on_delete=models.CASCADE)

class AdminPassword(models.Model):
    AdminID=models.CharField(max_length=10,primary_key=True)
    AdminName=models.CharField(max_length=20)
    Email_ID=models.CharField(max_length=50,unique=True)
    Role=models.CharField(max_length=10)
    Password=models.CharField(max_length=50)


    