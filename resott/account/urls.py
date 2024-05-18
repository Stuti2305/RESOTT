from django.urls import path

from .import views
urlpatterns=[
    path('',views.register,name='register'),
    path('RRegister',views.RRegister,name='RRegister'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='signout'),
    path('profile',views.dashboard,name='profile'),
    path('uprofile',views.updateprofile,name='uprofile'),
]