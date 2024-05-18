from django.urls import path
from . import views #from all import views

urlpatterns = [                      #to provide list of mappings
    path("",views.index,name="index"), #blank means homepg, here index is the function associated with homepg
    path("restabt/menu/<int:rid>",views.menu,name="menu"),
    path("booking",views.booking,name="booking"),
    path("contact",views.contact,name="contact"),
    path("register",views.register,name="register"),
    path("obooking",views.obooking,name="obooking"),      
    path("feed",views.Feedback,name="fd"),
    path("booktable",views.booktable,name="bktbl"),
    path("updaterestaurant",views.updaterestaurant,name="updaterestaurant"),
    path("search",views.search,name="search"),
    path("about",views.about,name="about"),
    path("cart", views.crt,name="cart"),
    path("change_quan",views.change_quan,name="change_quan"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("restabt/<int:rid>",views.restabt,name='restabt'),
    path("process_payment",views.process_payment,name="process_payment"),
    path("payment_done",views.payment_done,name="payment_done"),
    path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
     path("r_cart",views.r_cart,name="r_cart"),
]