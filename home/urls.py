from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("learn",views.learn,name='learn'),
    path("forms",views.forms,name='forms'),
    path("signup",views.handleSignup,name='handleSignup'),
    path("login",views.handleLogin,name='handleLogin'),
    path("logout",views.handleLogout,name='handleLogout'),
    path("earn",views.earn,name='earn'),
    path("grow",views.grow,name='grow'),
    path("full",views.full,name='full'),
    path("digital",views.digital,name='digital'),
    path("graphic",views.graphic,name='graphic'),
    path("checkout",views.checkout,name='checkout'),
    path("payout",views.payout,name='payout'),
]
