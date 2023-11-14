from django.shortcuts import render,HttpResponse

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
    return render(request,"contact.html")
    # return HttpResponse("Welcome to CONTACT page")
