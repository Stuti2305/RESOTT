from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)     
    profilepic=models.ImageField(upload_to="media/profileimages",default='default/profile.jpg')
    contactno=models.BigIntegerField(default='1000000000')
    address=models.TextField(blank=True)
    city=models.CharField(max_length=25,blank=True)
    updated_on=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.user.username
    

