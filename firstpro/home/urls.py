from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.service,name='services'),
    path("contact",views.contact,name='contact'),
]
