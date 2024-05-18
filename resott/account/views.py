from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import profile

def register(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        em=request.POST['email']
        cn=request.POST['contact']
        adres=request.POST['address']
        city=request.POST['city']
        pww=request.POST['pw']
        cpw=request.POST['cpw']
        if pww==cpw:
            if (User.objects.filter(username=un)).exists():     #user table
                messages.info(request,"UserName already exists")
                return redirect('register') 
            else:
                accntcrt=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=pww)
                accntcrt.save()
                ppf=profile(user=accntcrt,contactno=cn,city=city)   #match
                ppf.save()
                return redirect('login')
        else:
            messages.info(request,"Password doesnot match")
            return redirect('register')
        
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        un=request.POST['uname']
        pw=request.POST['pw']
        log=auth.authenticate(username=un,password=pw) #for authentication(matching)
        if log!=None:
            auth.login(request,log)
            messages.success(request,'congratulations! Welcome to RESOTT')
            return redirect('index')
            
        else:
            messages.warning(request,'Wrong Password or Username')
            return redirect('login')    
    return render(request,'login.html') 

def logout(request):  
    auth.logout (request) 
    return redirect('login')

def dashboard(request):
    dis={}
    proid=profile.objects.filter(user_id=request.user.id)
    if len(proid)>0:
        entry=profile.objects.get(user_id=request.user.id)
        dis['disent']=entry
    return render (request,"profile.html",dis)

def updateprofile(request):
    dis={}
    
    proid=profile.objects.filter(user_id=request.user.id)
    if len(proid)>0:
        entry=profile.objects.get(user_id=request.user.id)
        dis['disent']=entry
        if request.method=="POST":
            
            frn=request.POST["frn"]
            lan=request.POST["lan"]
            em=request.POST["em"]
            con=request.POST["con"]
            add=request.POST["add"]
            city=request.POST["city"]
            usr= User.objects.get(id=request.user.id)
            usr.first_name=frn
            usr.last_name=lan
            usr.email=em
            usr.save()
            entry.contactno=con
            entry.address=add
            entry.city=city
            entry.save()
            if "pimg" in request.FILES:
                pro_image=request.FILES["pimg"]
                entry.profilepic=pro_image
                entry.save()
            
    return render (request,"updateprofile.html",dis)

def RRegister(request):
    if request.method=='POST':
        on=request.POST['oname']
        un=request.POST['rname']
        em=request.POST['email']
        cn=request.POST['contact']
        city=request.POST['city']
        pww=request.POST['pw']
        cpw=request.POST['cpw']
        if pww==cpw:
            if (User.objects.filter(username=un)).exists():     #user table
                messages.info(request,"Restaurant already exists")
                return redirect('RRegister') 
            else:

                accntcrt=User.objects.create_user(username=un,first_name=on,email=em,password=pww)
                if "accept" in request.POST:
                    accntcrt.is_staff=True
                    accntcrt.save()
                ppf=profile(user=accntcrt,contactno=cn,city=city)   #match
                ppf.save()
                messages.success(request,'CONGRATULATIONS! Your restaurant details are successfully added to RESOTT')
                return redirect('RRegister')
        else:
            messages.info(request,"Password doesnot match")
            return redirect('RRegister')   
    return render(request,'RRegister.html')
