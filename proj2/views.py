from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from subprocess import run,PIPE
import sys, subprocess


def index(request):
    return render(request,'index.html')

def userreg(request):
      if request.method=='POST':
        photo=request.FILES['photo']
        up=FileSystemStorage()
        img=up.save(photo.name,photo)
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        log=complaint_box_register(name=name,email=email,password=password,photo=photo,phone=phone)
        log.save()
      return render(request,'register.html')

def userview(request):
    u=complaint_box_register.objects.all()
    return render(request,'viewuser.html',{'res':u})


def userlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['adminemail'] = email
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login successfull'} )

    elif complaint_box_register.objects.filter(email=email,password=password).exists():
        udet=complaint_box_register.objects.get(email=request.POST['email'],password=password)
        if udet.password == request.POST['password']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.name
            request.session['uemail'] = udet.email
            request.session['user'] = 'user'
            return render(request,'index.html',{'status': 'user login successfull'})

    else:
            return render(request, 'login.html', {'status': 'incorrect credentials'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for keys in session_keys:
        del request.session[keys]
    return redirect(index)
    

def uprofile(request):
    t=request.session['uid']
    g=complaint_box_register.objects.get(id=t)
    return render(request,'userprofile.html',{'res':g})

def aprofile(request):
    return render(request,'adminprofile.html')

def facreg(request):
      if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        designation=request.POST.get('designation')
        password=request.POST.get('password')
        log=complaint_box_faculty(name=name,email=email,password=password,designation=designation)
        log.save()
      return render(request,'facregister.html')


  
def facltylogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    designation = request.POST.get('designation')
    if complaint_box_faculty.objects.filter(email=email,designation=designation,password=password).exists():
        fac=complaint_box_faculty.objects.get(email=request.POST['email'],designation=request.POST['designation'],password=password)
        if fac.password == request.POST['password'] and fac.designation == request.POST['designation']:
            request.session['facid'] = fac.id
            request.session['facname'] = fac.name
            request.session['facemail'] = fac.email
            request.session['facdesig'] = fac.designation
            request.session['facuser'] = 'facuser'
            return render(request,'index.html',{'status': 'user login successfull'})

    else:
            return render(request, 'faclogin.html', {'status': 'incorrect credentials'})
    

def admlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['adminemail'] = email
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login successfull'} )
    else:
            return render(request, 'adminlogin.html', {'status': 'incorrect credentials'})
    
def facltyprofile(request):
    t=request.session['facid']
    g=complaint_box_faculty.objects.get(id=t)
    return render(request,'facultyprofile.html',{'res':g})

def facview(request):
    u=complaint_box_faculty.objects.all()
    return render(request,'viewfaculty.html',{'res':u})

def fdelete(request,id):
    mark=complaint_box_faculty.objects.get(pk=id)
    mark.delete()
    return redirect(facview)

def udelete(request,id):
    mark=complaint_box_register.objects.get(pk=id)
    mark.delete()
    return redirect(userview)

def compreg(request):
      f=request.session['uid']
      if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        complaintto=request.POST.get('complaintto')
        complaintmesg=request.POST.get('complaintmesg')
        log=complaint_box_complaint(name=name,email=email,date=date,complaintto=complaintto,complaintmesg=complaintmesg,userid=f)
        log.save()
      return render(request,'complaint.html')

def viewcomp(request):
    c=complaint_box_complaint.objects.all()
    return render(request,'complaintview.html',{'res':c})


def updatestatus(request,id):
    sid=complaint_box_complaint.objects.get(id=id)
    if request.method == 'POST'and complaint_box_complaint.objects.filter(status = "NotViewed"):
        sid.status = "Viewed"
        sid.save()

    elif request.method == 'POST'and complaint_box_complaint.objects.filter(status = "Viewed"):
        sid.status = "NotViewed"
        sid.save()
    return render(request, 'index.html')  
    

def acknmesg(request):
      if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        ackmesg=request.POST.get('ackmesg')
        log=complaint_box_acknowledgement(name=name,email=email,date=date,ackmesg=ackmesg)
        log.save()
      return render(request,'acknwldgmnt.html')

def acknview(request):
    c=complaint_box_acknowledgement.objects.all()
    return render(request,'acknwldgview.html',{'res':c})
   
 
def admack(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        designation=request.POST.get('designation')
        ackmesg=request.POST.get('ackmesg')
        log=complaint_box_facack(name=name,email=email,date=date,designation=designation,ackmesg=ackmesg,)
        log.save()
    return render(request,'adminack.html')

def adackview(request):
    c=complaint_box_facack.objects.all()
    return render(request,'admackview.html',{'res':c})

def cupdate(request,id):
    mark=complaint_box_register.objects.get(pk=id)
    return render(request,'upduserprof.html',{'res':mark})

def updates(request,id):
      f=request.session['uid']
      if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        log=complaint_box_register(name=name,email=email,password=password,phone=phone,id=id)
        log.save()
      return redirect(uprofile)
      return render(request,'index.html')   


    
    
    
