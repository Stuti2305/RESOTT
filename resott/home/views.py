from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse,JsonResponse
from .models import courses,restaurant
from .models import *
from django.contrib.auth.models import User
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from home.models import profile

#here in this file we create functions that are used in urls of home

def index(request):
    dic={}    #code written in {} is dynamic,its called jinja pattern
    rest=restaurant.objects.all().order_by("name")
    dic['key']=rest
    return render (request,"index.html",dic)  #this will send the response

def restabt(request,rid):
    dis={}
    roid=restaurant.objects.get(id=rid)
    entry=restprofile.objects.filter(rest=roid)
    #restuser=restaurant.objects.filter(usr=request.user).exists()
    #breakpoint()
    if request.user==roid.usr:
        dis["owner_status"]=True

    dis['diy']=entry
    feeds=feedback.objects.filter(rest=rid)
    dis["feed"]=feeds
    return render (request,"booking.html",dis)

def booktable(request):
    dic={}
    usr=get_object_or_404(User,id=request.user.id) #current logged in user
    if request.method=="POST":
        re=request.POST["rid"] 
        eml=request.POST["em"]
        cont=request.POST["cn"]
        time=request.POST["slt"]
        dte=request.POST["dt"]
        per=request.POST["per"]
        if re:

            res=get_object_or_404(restaurant,id=re) #checking for rest
            book=table(rest=res,customer=usr,email=eml,contactno=cont,time=time,date=dte,people=per) #db
            book.save()
            resta=restaurant.objects.get(id=res.id)

            if resta.status_full==False:
                rest0=FoodANDcombo.objects.filter(res=resta , type=4)
                rest1=FoodANDcombo.objects.filter(res=resta , type=1)
                rest2=FoodANDcombo.objects.filter(res=resta , type=5)
                rest3=FoodANDcombo.objects.filter(res=resta , type=6)
                rest4=FoodANDcombo.objects.filter(res=resta , type=7)
                rest5=FoodANDcombo.objects.filter(res=resta , type=8)
                rest6=FoodANDcombo.objects.filter(res=resta , type=9)
                rest7=FoodANDcombo.objects.filter(res=resta , type=10)
                dic["cro"]=rest0
                dic["cro1"]=rest1
                dic["cro2"]=rest2
                dic["cro3"]=rest3
                dic["cro4"]=rest4
                dic["cro5"]=rest5
                dic["cro6"]=rest6
                dic["cro7"]=rest7
            else:
                dic["msg"]="🚫🚫This Restaurant is not available right now"
        else:
            dic["msg"]="🚫🚫This Restaurant is busy"
        return render(request,"menu extra.html",dic)

def about(request):
    return render (request,"about.html")
    
def booking(request):
    return render (request,"booking.html")

def register(request):    
    return render (request,"register.html") 

def obooking(request):    
    return render (request,"obooking.html")       

def contact(request):
    return render (request,"contact.html")
  
def menu(request,rid):
    dic={}
    resta=restaurant.objects.get(id=rid)
    if resta.status_full==False:
        rest0=FoodANDcombo.objects.filter(res=resta , type=4)
        rest1=FoodANDcombo.objects.filter(res=resta , type=1)
        rest2=FoodANDcombo.objects.filter(res=resta , type=5)
        rest3=FoodANDcombo.objects.filter(res=resta , type=6)
        rest4=FoodANDcombo.objects.filter(res=resta , type=7)
        rest5=FoodANDcombo.objects.filter(res=resta , type=8)
        rest6=FoodANDcombo.objects.filter(res=resta , type=9)
        rest7=FoodANDcombo.objects.filter(res=resta , type=10)
        dic={"cro":rest0,"cro1":rest1,"cro2":rest2,"cro3":rest3,"cro4":rest4,"cro5":rest5,"cro6":rest6,"cro7":rest7}
    else:
        dic["msg"]="🚫🚫This Restaurant is not available right now"
    return render (request,"menu extra.html",dic) 

def updaterestaurant(request):
    dis2={}
    res=restaurant.objects.filter(usr=request.user)
    
    if res:
        
        
    #if res==None:
        #messages.error(request,'you are unauthorized for this restaurant')
        restaurant_ids = res.values_list("id", flat=True)
        #entry=restprofile.objects.get(rest_id=res.values("id"))
        entry = restprofile.objects.filter(rest_id__in=restaurant_ids).first()
        dis2['disent2']=entry
        if request.method=="POST":
            lo=request.POST["lo"]
            d=request.POST["d"]
        
            o=request.POST["o"]
            t=request.POST["t"]
            ab=request.POST["ab"]
            c=request.POST["c"]
            co=request.POST["co"]
            dis=request.POST["dis"]
            entry.localty=lo
            entry.timings=t
            entry.details=d
            entry.costEstimate=c
            entry.contact=co
            
            rid=res[0].id
            entry.overview=o
            entry.about=ab
            if dis:
                breakpoint()
                res.dis=dis
                res.save()
            
            entry.save()
            
            if "pimg" in request.FILES:
                pro_image=request.FILES["pimg"]
                res.cimage=pro_image
                res.save()
                return redirect(index)
            return redirect(restabt,rid=rid)
        
        if request.user.id!=res[0].usr_id:
            messages.error(request,'you are unauthorized for this restaurant')
    return render (request,"updaterestaurant.html",dis2)   
    
def search(request):
    dic={}
    if request.method=='GET':
        sr=request.GET['search']
        xyz=FoodANDcombo.objects.filter(dish__icontains=sr)
        if len(xyz)>0:
            dic['cro']=xyz
        else:
            restaurant.objects.filter(name__icontains=sr)
            dic['cro']=xyz 
    return render (request,"menu extra.html",dic)    

def crt(request):
    dic={}
    items=cart.objects.filter(user__id=request.user.id,status=False) 
    dic['items']=items
    if request.user.is_authenticated:
        if request.method=="POST":
            cartid=request.POST["ct"]
            quantity=request.POST["qty"]
            is_exist=cart.objects.filter(rest_id=cartid, user_id=request.user.id, status=False)
            if len(is_exist)>0:
                dic["msg"]="This dish already exists. Do you want to repeat??"
            else:
                usr=get_object_or_404(User,id=request.user.id)  
                cor=get_object_or_404(FoodANDcombo,id=cartid)
                
                crt=cart(user=usr,rest=cor,quantity=quantity)
                crt.save()
                dic["msg"]="Item added to cart"
    else:
        dic["msg"]="login first"
    return render (request,"book.html",dic)
def r_cart(request):
    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cartobj = get_object_or_404(cart, id=id)
        cartobj.delete()
    return HttpResponse(1)
    
def get_cart_data(request):
    items = cart.objects.filter(user__id=request.user.id, status=False)
    sale,quantity,dis =0,0,5
    for i in items:
        sale += float(i.rest.price)*i.quantity+500
        dis+=sale*i.rest.res.dis/100
        quantity+= float(i.quantity)
        grand=sale-dis

    res = {
        "offer":sale,"quan":quantity,"dis":dis,"gt":grand

    }
    return JsonResponse(res)
    
def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

def process_payment(request):
    dit={}
    res=table.objects.filter(customer=request.user.id)
    

    dit['tbl']=res
    
    items = cart.objects.filter(user_id__id=request.user.id,status=False)
    dit["itm"]=items
    products=""
    amt=0
    inv = "INV10001-"
    cart_ids = ""
    p_ids =""
    for j in items:
        products += str(j.rest.dish)+"\n"
        p_ids += str(j.rest.id)+","
        
        dis=int(j.rest.res.dis)
        if dis>0:
            amt += (float(j.rest.price)+500)
            dis+=amt*float(j.rest.res.dis)/100
            amt =amt-dis
            inv +=  str(j.id)
            cart_ids += str(j.id)+","
        else:
            amt += float(j.rest.price)+500
            inv +=  str(j.id)
            cart_ids += str(j.id)+","
        
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt/77),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
    usr = User.objects.get(username=request.user.username)
    ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
    ord.save()
    ord.invoice_id = str(ord.id)+inv
    ord.save()
    request.session["order_id"] = ord.id
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    dit["form"]=form
    return render(request, 'process_payment.html',dit)

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")

def payment_cancelled(request):
    return render(request,"payment_failed.html")    
    
def Feedback(request):
    usr=get_object_or_404(User,id=request.user.id)
    prf=profile.objects.get(user_id=request.user.id)
    
    if request.user.is_authenticated:
        if request.method=='POST':
            brid=request.POST['brid']
            mes=request.POST['comments']
            rate=request.POST['rat']
            
            br=get_object_or_404(restaurant,id=brid)
            fdcr=feedback(user=usr,prf=prf,rest=br,msg=mes,rating=rate)
            fdcr.save()
            return redirect('index')
            
    return render(request,"booking.html")