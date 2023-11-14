from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    variable = {
        "new_var" : "TEAM UP"
    }
    return render(request,"index.html")             #render used to request the templates
    # return HttpResponse("Welcome to HOME page")            #httpresponse to return the string 
def about(request):
    return render(request,"about.html")
    # return HttpResponse("Welcome to ABOUT page")
def service(request):
    return render(request,"services.html")
    # return HttpResponse("Welcome to SERVICES page")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Message sent")

    return render(request,"contact.html")
    # return HttpResponse("Welcome to CONTACT page")
