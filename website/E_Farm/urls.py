from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home),
    path("farmer-registration/",farmerReg),
    path("farmer-login/",farmerLog),
    path("add-product/",addPro),
    path("user-registration/",userReg),
    path("user-login/",userLog),
    path("about-us/",aboutUs),
    path("contact-us/",contactUs),
    path("cart/",cart),
    path("checkout/",checkout),


]