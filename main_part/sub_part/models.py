from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField
from django.shortcuts import redirect, render

# Create your models here.
class message(models.Model):
    yourname=models.CharField(max_length=100)
    mailid=models.EmailField()
    txtarea=models.CharField(max_length=1000)

    def __str__(self):
        return self.yourname

class usign(models.Model):
    email=models.EmailField()
    Username=models.CharField(max_length=100)
    passwrd=models.CharField(max_length=32)
    rpass=models.CharField(max_length=32)

    def __str__(self):
        return self.email


class asign(models.Model):
    emailid=models.EmailField()
    Username=models.CharField(max_length=100)
    password1=models.CharField(max_length=32)
    password2=models.CharField(max_length=32)

    def __str__(self):
        return self.Username



class uaddevent(models.Model):
    aeventname=models.CharField(max_length=50)
    adate=models.DateField('%Y:%m:%d;%H:%M')
    acategorize=models.CharField(max_length=12)
    nomembers=models.CharField(max_length=10)
    atime=models.TimeField()
    amountperone=models.CharField(max_length=10000000)
    adescription=models.CharField(max_length=100000)
    Aaddress=models.CharField(max_length=500)
    aimage=models.ImageField(upload_to='aimage',null=True,blank=True)
    aservices=models.CharField(max_length=500)
    youtube=models.URLField()

    def __str__(self):
        return self.adate



class proedituser(models.Model):
    userp=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    gender=models.CharField(max_length=4)
    address=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
        return self.userp

class profileu(models.Model):
    usern=models.CharField(max_length=40)
    uGender=models.CharField(max_length=12)
    homead=models.CharField(max_length=100)
    eid=models.CharField(max_length=50)
    phnum=models.CharField(max_length=11)
    


    def __str__(self):
        return self.usern

    
class myprofile(models.Model):
    myname=models.CharField(max_length=100)
    mygender=models.CharField(max_length=12)
    myaddress=models.CharField(max_length=200)
    myemail=models.EmailField()
    myphn=models.CharField(max_length=15)

    def __str__(self):
        return self.myname


class adevents(models.Model):
    aeventname=models.CharField(max_length=100)
    adate=models.DateField()
    acategorize=models.CharField(max_length=12)
    nomembers=models.CharField(max_length=1000)
    atime=models.TimeField()
    amountperone=models.CharField(max_length=100000)
    adescription=models.CharField(max_length=1000)
    Aaddress=models.CharField(max_length=500)
    aimage=models.ImageField(upload_to='aimage',null=True,blank=True)
    aservices=models.CharField(max_length=100)
    youtube=models.URLField()

    def __str__(self):
        return self.aeventname




class Manualbooking(models.Model):
    matches=models.CharField(max_length=12)
    customername=models.CharField(max_length=100)
    customerid=models.CharField(max_length=100)
    customerPhoneNo=models.CharField(max_length=15)
    customeraddress=models.CharField(max_length=1000)
    ticketcount=models.CharField(max_length=1000)
    bookingperson=models.CharField(max_length=100)
    paymentamount=models.CharField(max_length=100000)
    status=models.CharField(max_length=12)
    confirmation=models.CharField(max_length=2)

    def __str__(self):
        return self.matches



class adminuser(models.Model):
    Nameofuser=models.CharField(max_length=100)
    userEmail=models.EmailField()
    userPassword=models.CharField(max_length=100)
    Planname=models.CharField(max_length=100)
    verification=models.CharField(max_length=2)

    def __str__(self):
        return self.Nameofuser





class AdminContacts(models.Model):
    contactmail=models.EmailField()
    showmail=models.CharField(max_length=2)
    contactPhone=models.CharField(max_length=15)
    shownumber=models.CharField(max_length=15)
    contactaddress=models.CharField(max_length=100)
    showAddress=models.CharField(max_length=100)
    sendmail=models.CharField(max_length=2)
    adminstatus=models.CharField(max_length=2)
    showDatabase=models.CharField(max_length=2)

    def __str__(self):
        return self.contactmail


class AddMembership(models.Model):
    NAMEofPLAN=models.CharField(max_length=50)
    PlanType=models.CharField(max_length=100)
    PlanPrice=models.CharField(max_length=100)
    PlanStatus=models.CharField(max_length=100)

    def __str__(self):
        return self.NAMEofPLAN


class paymentevent(models.Model):
    cardnumber=models.CharField(max_length=100)
    expiration=models.CharField(max_length=100)
    cvv=models.CharField(max_length=100)
    cardowner=models.CharField(max_length=100)
    
    def __str__(self):
        return self.cardowner











































    









