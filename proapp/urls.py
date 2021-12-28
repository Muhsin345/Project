from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.fnprod,name="products"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.fnsignup,name="signup")
]