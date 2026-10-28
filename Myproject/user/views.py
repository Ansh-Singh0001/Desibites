from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):

    x=category.objects.all()
    d={"cat":x}
    return render(request,"index.html",d)
    
    
def contact(request):
    d={}
    if request.method=="POST":
        a1=request.POST.get("name")#ram
        a2=request.POST.get("email")#abc@gmail.com
        a3=request.POST.get("mob")#7390838645
        a4=request.POST.get("msg")#hello
        #d={"x1":name,"x2":email,"x3":mobile,"x4":message}
        Contactus(name=a1,email=a2,mobile=a3,message=a4).save()
        return HttpResponse("<script>alert('data added successfully..');location.href='/contact/';</script>")
    return render(request,"contact.html",d)

def gallery(request):
    data=igallery.objects.all()
    d={"gdata":data}

    return render(request,"gallery.html",d)

def wchoose(request):
    return render(request,"wchoose.html")

def team(request):
    return render(request,"team.html")

def mybooking(request):
    x=category.objects.all()
    d={"cat":x}
    if request.method=="POST":
        a1=request.POST.get("name")#ram
        a2=request.POST.get("mob")#abc@gmail.com
        a3=request.POST.get("totalperson")#7390838645
        a4=request.POST.get("date")#hello
        a5=request.POST.get("time")#time
        a6=request.POST.get("foodtypemain")#time
        a7=request.POST.get("foodtype")#time
        a8=request.POST.get("email")#time
        a9=request.POST.get("pmode")#time
        #d={"x1":name,"x2":email,"x3":mobile,"x4":message}
        booking(name=a1,mobno=a2,email=a8,totalperson=a3,date=a4,time=a5,foodtype=a6,mealtype=a7,paymode=a9).save()
        return HttpResponse("<script>alert('We have received your booking.We will call your back soon..');location.href='/booking/';</script>")
   
    return render(request,"booking.html",d)

def foodmenu(request):
     id=request.GET.get('id')
     if id:
         x=menu.objects.filter(category=id)
     else:
         x=menu.objects.all()
         d={"mdata":x}
     return render(request,"foodmenu.html",d)
 
def services(request):
    return render(request,"services.html")
