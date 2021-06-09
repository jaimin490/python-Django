from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name='home'),
    path('about',views.aboutpageview,name='about'),
    path('contact',views.contactpageview,name='contact'),
    path('form',views.myform,name='myform'),
    path('formprocess',views.process,name='process'),
    path('register',views.register,name='register'),
    path('regProcess',views.reg,name='reg'),
]
