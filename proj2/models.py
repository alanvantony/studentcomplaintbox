from django.db import models

class complaint_box_register(models.Model):
    photo=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    password=models.CharField(max_length=200)


class complaint_box_faculty(models.Model):
    designation=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class complaint_box_complaint(models.Model):
    userid=models.CharField(max_length=200)
    complaintto=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    complaintmesg=models.CharField(max_length=2000)
    status=models.CharField(max_length=200,default = "NotViewed")

class complaint_box_acknowledgement(models.Model):
    name=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    ackmesg=models.CharField(max_length=200)

class complaint_box_facack(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    ackmesg=models.CharField(max_length=200)
    
