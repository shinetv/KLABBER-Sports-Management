from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from . models import message
from . models import usign
from . models import asign
from . models import adevents
from . models import Manualbooking
from . models import adminuser
from . models import AdminContacts
from . models import AddMembership
from . models import paymentevent
from . models import uaddevent
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
import easygui



# Create your views here.
def home(request):
    return render(request,'home.html')

def homemsg(request):
    if request.method=='POST':
        msg_dis=message(yourname=request.POST['yourname'],
                        mailid=request.POST['mailid'],
                        txtarea=request.POST['txtarea']       
                        )
        msg_dis.save()
        easygui.msgbox("your queries send successfully.....!")
        return redirect(home)

    return render(home) 

def userl(request):
    if request.method=='POST':
        if usign.objects.filter(Username=request.POST['Username'],passwrd=request.POST['passwrd']).exists():
            users_dis=usign.objects.get(Username=request.POST['Username'],passwrd=request.POST['passwrd'])
            easygui.msgbox("Log in successfully.....!")
            return render(request,'user Dashboard.html',{'users_dis':users_dis})
        else:
            context={'msg':'You Entered wrong Password or Username'}
            return render(request,'userlogin.html',context)


    return render(request,'userlogin.html') 
def users(request):
    if request.method=='POST':
        if usign.objects.filter(Username=request.POST['Username']):
            easygui.msgbox(" Username already taken")
        else:

            users_dis=usign(email=request.POST['email'],
                        Username=request.POST['Username'],
                        passwrd=request.POST['passwrd'],
                        rpass=request.POST['rpass']
                        )
            if users_dis.passwrd == users_dis.rpass :

               users_dis.save()
               easygui.msgbox("sign up successfull....!")
               return redirect(userl)
            else:
                easygui.msgbox("Passwords didnt match") 
                return redirect(users)  

    return render(request,'user-signup.html') 

def userdashboard(request):
    return render(request,'user Dashboard.html')



def uevent(request):
    if request.method=='POST':
        adding=adevents()
        adding.aeventname=request.POST.get('aeventname')
        adding.adate=request.POST.get('adate')
        adding.acategorize=request.POST.get('acategorize')
        adding.nomembers=request.POST.get('nomembers')
        adding.atime=request.POST.get('atime')
        adding.amountperone=request.POST.get('amountperone')
        adding.adescription=request.POST.get('adescription')
        adding.Aaddress=request.POST.get('Aaddress')
        if len(request.FILES)!=0:
            adding.aimage=request.FILES['aimage']
        adding.aservices=request.POST.get('aservices')
        adding.youtube=request.POST.get('youtube')
        adding.save()
        easygui.msgbox("Redirect to Payment")
        return redirect(Bankpayment)
        

    return render(request,'Add event.html')


def logout(request):
    log(request)
    easygui.msgbox("Logged out")
    return render(request,'userlogin.html')

       


                             
    
def upast(request):
    events=adevents.objects.all()
    context={'events':events}
    return render(request,'Past events.html',context) 


def ubookdetail(request):
    products=adevents.objects.all()
    context={'products':products}
    return render(request,'Booking detail.html',context)


def editbook(request,id):
    edit1=adevents.objects.get(id=id)
    return render(request,'booking detailedit.html',{'edit1':edit1})


def updatebook(request,id):
    edit1=adevents(id=id,aeventname=request.POST['aeventname'],
                    amountperone=request.POST['amountperone'],
                    nomembers=request.POST['nomembers'],
                    adate=request.POST['adate'],
                    atime=request.POST['atime']
                    )
    edit1.save()
    easygui.msgbox("Successfully Updated")
    return redirect(ubookdetail)



def uprofile(request):
    profile=usign.objects.all()
    context6={'profile':profile}
    return render(request,'Profile.html',context6)
   

def uedit(request,id):
    var=usign.objects.get(id=id)
    context={'var':var}
    return render(request,'Edit profile.html',context)

def editprofile(request,id):
    var=usign(id=id,email=request.POST['email'],
              Username=request.POST['Username'],
              passwrd=request.POST['passwrd']
              )
    var.save()
    easygui.msgbox("Profile updated successfully")
    return redirect(uprofile)

def uchangepass(request,id):
    var2=usign.objects.get(id=id)
    context={'var2':var2}
    return render(request,'Change Password.html',context)


def updateprofile(request,id):
    var2=usign(id=id,email=request.POST['email'],
               Username=request.POST['Username'],
               passwrd=request.POST['passwrd'],
               rpass=request.POST['rpass']
               
              )
    var2.save()
    easygui.msgbox(" Your password changed sucessfully")
    return redirect(uprofile) 

def deleteprofile(request,id):
    var2=usign.objects.get(id=id)
    var2.delete()
    easygui.msgbox("Deleted Successfully")
    return redirect(uprofile)    
    
                  
    


def upurchase(request):
    return render(request,'Purchase plan.html')


def adminavailable(request):
    available=AdminContacts.objects.all()
    context5={'available':available}
    return render(request,'UserADMIN.html',context5)   


def Bankpayment(request):
    if request.method=='POST':
        pay=paymentevent(cardnumber=request.POST['cardnumber'],
                         expiration=request.POST['expiration'],
                         cvv=request.POST['cvv'],
                         cardowner=request.POST['cardowner']
                         )
        pay.save()
        easygui.msgbox("THANKYOU")
        return redirect(paymentsuccess)                 
    return render(request,'Payment user.html')   

def paymentsuccess(request):
    return render(request,'payment done.html')

def eimage(request):
    return render(request,'carousell.html')   

def storyfeed(request):
    return render(request,'news feed.html')     
  


#adminside---------------------------------------------------------------------------->

def admlog(request):
    if request.method=='POST':
        if asign.objects.filter(emailid=request.POST['emailid'],password1=request.POST['password1']).exists():
            admsign_dis=asign.objects.get(emailid=request.POST['emailid'],password1=request.POST['password1'])
            easygui.msgbox("WELCOMES YOU NEW ADMIN!")
            return redirect(dashboard)
        else:
            context={'msg':'You Entered wrong Password or Username'}
            return render(request,'adminlogin1.html',context)    
    return render(request,'adminlogin1.html')


def admsign(request):
    if request.method=='POST':
        if asign.objects.filter(Username=request.POST['Username']):
            easygui.msgbox(" Username already taken")
        else:
          admsign_dis=asign(emailid=request.POST['emailid'],
                           Username=request.POST['Username'],
                           password1=request.POST['password1'],
                           password2=request.POST['password2']
                        )
        if admsign_dis.password1 == admsign_dis.password2 :
          admsign_dis.save()
          easygui.msgbox("Admin signup successfull......!")
          return redirect(admlog)
        else:
            easygui.msgbox("Passwords didnt match") 
            return redirect(admsign)                     
    return render(request,'adminsignup1.html') 


def dashboard(request):
    return render(request,'admin index.html')


def adevent(request):
    if request.method=='POST':
        prod=adevents()
        prod.aeventname=request.POST.get('aeventname')
        prod.adate=request.POST.get('adate')
        prod.acategorize=request.POST.get('acategorize')
        prod.nomembers=request.POST.get('nomembers')
        prod.atime=request.POST.get('atime')
        prod.amountperone=request.POST.get('amountperone')
        prod.adescription=request.POST.get('adescription')
        prod.Aaddress=request.POST.get('Aaddress')
        if len(request.FILES)!=0:
            prod.aimage=request.FILES['aimage']
        prod.aservices=request.POST.get('aservices')
        prod.youtube=request.POST.get('youtube')
        prod.save()
        easygui.msgbox("added Successfully")
        return redirect(adevent)

    return render(request,'admin Add event.html')


def adManageEvent(request):
    prod1=adevents.objects.all()
    context1={'prod1':prod1}
    return render(request,'admin Manage event.html',context1) 


def adbookedit(request,id):
    aedit=adevents.objects.get(id=id)
    return render(request,'adminbookingedit.html',{'aedit':aedit})


def updateadbook(request,id):
    aedit=adevents(id=id,aeventname=request.POST['aeventname'],
                   amountperone=request.POST['amountperone'],
                   nomembers=request.POST['nomembers'],
                   adate=request.POST['adate'],
                   atime=request.POST['atime']
                  )
    aedit.save()
    easygui.msgbox("Successfully Changed!")
    return redirect(adManageEvent)


def deleteadbook(request,id):
    aedit=adevents.objects.get(id=id)
    aedit.delete()
    easygui.msgbox("Deleted Successfully!")                
    return redirect(adManageEvent)


def adTotal(request):
    totalcollection=adevents.objects.all()
    context={'totalcollection':totalcollection}
    return render(request,'admin Total collection.html',context)    


def adminPast(request):
    pastevent=adevents.objects.all()
    context={'pastevent':pastevent}
    return render(request,'admin Past events.html',context)



def BookingDetails(request):
    booking=Manualbooking.objects.all()
    context2={'booking':booking}
    return render(request,'admin Bookingdetail.html',context2) 


def manualedit(request,id):
    bookedit=Manualbooking.objects.get(id=id)
    return render(request,'admin manualedit.html',{'bookedit':bookedit}) 

def manualupdate(request,id):
    bookedit=Manualbooking(id=id,customername=request.POST['customername'],
                           customerid=request.POST['customerid'],
                           ticketcount=request.POST['ticketcount'],
                           bookingperson=request.POST['bookingperson'],
                           paymentamount=request.POST['paymentamount'],
                           status=request.POST['status']
                        )
                          
    bookedit.save()
    easygui.msgbox("Updated Successfully!")
    return redirect(BookingDetails)                    



def adminmanual(request):
    if request.method=='POST':
        manual=Manualbooking(matches=request.POST['matches'],
                            customername=request.POST['customername'],
                            customerid=request.POST['customerid'],
                            customerPhoneNo=request.POST['customerPhoneNo'],
                            customeraddress=request.POST['customeraddress'],
                            ticketcount=request.POST['ticketcount'],
                            bookingperson=request.POST['bookingperson'],
                            paymentamount=request.POST['paymentamount'],
                            status=request.POST['status'],
                            confirmation=request.POST['confirmation']
                            )
        manual.save()
        subject='KLABBER WELCOMES YOU '
        message='Thankyou for your interest, Your booking completed successfully....'
        email_from=settings.EMAIL_HOST_USER
        recepient=request.POST.get('customerid')
        print("check:",recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)
        easygui.msgbox(" Your Event Booked Successfully  !")
        return redirect(BookingDetails)                    
        
    return render(request,'admin Manual Booking.html')   



def adminProfile(request):
    adp=asign.objects.all()
    context={'adp':adp}
    return render(request,'admin Profile.html',context)

def EditProfile(request,id):
    varr=asign.objects.get(id=id)
    context={'varr':varr}
    return render(request,'admin Edit profile.html',context)  

def admineditprofile(request,id):
    varr=asign(id=id,emailid=request.POST['emailid'],
               Username=request.POST['Username'],
               password1=request.POST['password1']
               )
    varr.save()
    easygui.msgbox("Profile updated successfully")
    return redirect(adminProfile)

def adminchangepassword(request,id):
    admchange=asign.objects.get(id=id)
    return render(request,'admin Change Password.html',{'admchange':admchange})


def updateadminpass(request,id):
    admchange=asign(id=id,emailid=request.POST['emailid'],
    Username=request.POST['Username'],
    password1=request.POST['password1'],
    password2=request.POST['password2'])

    admchange.save()
    easygui.msgbox("Password Updated Succesfully !")
    return redirect(adminProfile)

def DeleteadPass(request,id):
    var=asign.objects.get(id=id)
    var.delete()
    easygui.msgbox("Data Deleted Successfully !")
    return redirect(adminProfile)    


   


def adminadduser(request):
    if request.method=='POST':
        adminad=adminuser(Nameofuser=request.POST['Nameofuser'],
                          userEmail=request.POST['userEmail'],
                          userPassword=request.POST['userPassword'],
                          Planname=request.POST['Planname'],
                          verification=request.POST['verification']
                          )
        adminad.save()
        subject = ' KLABBER WELCOMES YOU'
        message = 'Thank you for  your support and intrest towards klabber'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('userEmail')
        print("check:",recepient)
        send_mail(subject,message, email_from, [recepient], fail_silently = False)
        easygui.msgbox("Successfully Added!...") 
        return redirect(adminadduser)                 
    return render(request,'admin Add user.html')


def adminmanageuser(request):
    manage=adminuser.objects.all()
    context3={'manage':manage}
    return render(request,'admin Manage user.html',context3)
    

def editmanager(request,id):
    manageedit=adminuser.objects.get(id=id)
    return render(request,'manage user edit.html',{'manageedit':manageedit})


def manageupdate(request,id):
    manageedit=adminuser(id=id,Nameofuser=request.POST['Nameofuser'],
                        userEmail=request.POST['userEmail'],
                        Planname=request.POST['Planname']
                        )
    manageedit.save()
    easygui.msgbox("Thank you for Updation...!")
    return redirect(adminmanageuser)   


def managedlt(request,id):
    manageedit=adminuser.objects.get(id=id)
    manageedit.delete()
    easygui.msgbox("DELETED.......!")
    return redirect(adminmanageuser)


def ship(request):
    if request.method=='POST':
       adding_ship=AddMembership(NAMEofPLAN=request.POST['NAMEofPLAN'],
                                PlanType=request.POST['PlanType'],
                                PlanPrice=request.POST['PlanPrice'],
                                PlanStatus=request.POST['PlanStatus']
                                )
       adding_ship.save()
       easygui.msgbox("welcome to KLABBER !")
       return redirect(Manageship)
    return render(request,'admin Add membership plan.html')


def Manageship(request):
   table=AddMembership.objects.all()
   context={'table':table}
   return render(request,'admin Manage membership plan.html',context)


def shipform(request,id):
   var=AddMembership.objects.get(id=id)
   return render(request,'membership form.html',{'var':var})   


def update(request,id):
   var=AddMembership(id=id,NAMEofPLAN=request.POST['NAMEofPLAN'],
                  PlanType=request.POST['PlanType'],
                  PlanPrice=request.POST['PlanPrice'],
                  PlanStatus=request.POST['PlanStatus']
                  )
   var.save()
   easygui.msgbox("UPDATED SUCCESSFULLY")
   return redirect(Manageship)

def delete(request,id):
   var=AddMembership.objects.get(id=id)
   var.delete()
   easygui.msgbox("YOUR DATA HAS BEEN DELETED SUCCESSFULLY")
   return redirect(Manageship)


def Planrequest(request):
    preq=AddMembership.objects.all()
    context={'preq':preq}
    return render(request,'admin plan request.html',context)


def planedit(request,id):
    planreq=AddMembership.objects.get(id=id)
    return render(request,'planReqedit.html',{'planreq':planreq}) 


def planupdate(request,id):
    planreq=AddMembership(id=id,NAMEofPLAN=request.POST['NAMEofPLAN'],
                         PlanStatus=request.POST['PlanStatus']
                         ) 
    planreq.save()
    easygui.msgbox("Request Accepted Successfully")
    return redirect(Planrequest)


def PAYEVENT(request):
    payonline=paymentevent.objects.all()
    context={'payonline':payonline}
    return render(request,'event payment.html',context)                               


def adminContactus(request):
    if request.method=='POST':
        adcontactus=AdminContacts(contactmail=request.POST['contactmail'],
                                 showmail=request.POST['showmail'],
                                 contactPhone=request.POST['contactPhone'],
                                 shownumber=request.POST['shownumber'],
                                 contactaddress=request.POST['contactaddress'],
                                 showAddress=request.POST['showAddress'],
                                 sendmail=request.POST['sendmail'],
                                 adminstatus=request.POST['adminstatus'],
                                 showDatabase=request.POST['showDatabase']
                                 )
        adcontactus.save()
        subject=' KLABBER WELCOMES YOU'
        message='Thankyou for choosing KLABBER'
        email_from=settings.EMAIL_HOST_USER
        recepient=request.POST.get('contactmail')
        print("check:",recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)
        easygui.msgbox("Added successfully in Userpanel...!")
        return redirect(adminContactus)                         
    
    return render(request,'admin Contact us.html')


def contactusedit(request,id):
    contactedit=AdminContacts.objects.get(id=id) 
    return render(request,'contactusedit.html',{'contactedit':contactedit})        



def adminContactmanage(request):
    mesg=message.objects.all()
    context4={'mesg':mesg}
    return render(request,'admin Manage contact.html',context4)



    



 




