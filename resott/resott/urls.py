from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),   #now project resott will also include urls of our custom app named home
                                     #if searching for homepage look for home urls
    path('account/',include('account.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)