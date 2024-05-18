from distutils.command.upload import upload
from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import *
from django.forms import SlugField
from account.models import profile

class restaurant(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    status_full=models.BooleanField(default=True)
    name=models.CharField(max_length=25)
    details=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    cimage=models.ImageField(upload_to='media/restro')
    added_on=models.DateTimeField(auto_now_add=True)
    dis=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class courses(models.Model):
    crs=models.CharField(max_length=75,default="recommended")
    def __str__(self):
        return self.crs
    
class FoodANDcombo(models.Model):
    type=models.ForeignKey(courses,on_delete=models.CASCADE)
    res=models.ForeignKey(restaurant,on_delete=models.CASCADE)
    dish=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=25)
    fimage=models.ImageField(upload_to='media/restro')
    added_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.dish
class restprofile(models.Model):
    rest=models.ForeignKey(restaurant, on_delete=models.CASCADE)
    overview=models.CharField(max_length=100)
    about=models.CharField(max_length=1000)
    localty=models.CharField(max_length=30)
    timings=models.CharField(max_length=30)
    costEstimate=models.CharField(max_length=30)
    contact=models.CharField(max_length=25)
    directions=models.CharField(max_length=10000)
    
    img1=models.ImageField(upload_to="media/restro",default='default/default restaurant.jpg')
    img2=models.ImageField(upload_to="media/restro",default='default/default restaurant.jpg')
    img3=models.ImageField(upload_to="media/restro",default='default/default restaurant.jpg')
    updated_on=models.DateTimeField(auto_now=True,null=True) 
    map=models.URLField(default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d227822.55035627162!2d80.8024271802209!3d26.84862299412667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399bfd991f32b16b%3A0x93ccba8909978be7!2sLucknow%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1652175194751!5m2!1sen!2sin")


class cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    rest=models.ForeignKey(FoodANDcombo,on_delete=models.CASCADE)
   
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    updated_on=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.rest.dish  


class table(models.Model):
    rest=models.ForeignKey(restaurant,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=200)
    contactno=models.CharField(max_length=100)
    time=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    people=models.IntegerField(default=0)
    updated_on=models.DateTimeField(auto_now=True,null=True)

class Order(models.Model):
    cust_id = models.ForeignKey(User,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)

    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cust_id.username    

class feedback(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    prf=models.ForeignKey(profile, on_delete=models.CASCADE)
   
    rest=models.ForeignKey(restaurant,on_delete=models.CASCADE)
    rating=models.CharField(max_length=250)
    msg=models.TextField()
    added_on=models.DateTimeField(auto_now=True,null=True)
    def _str_(self):
        return self.user.username