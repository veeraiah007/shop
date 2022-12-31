from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from suba.form import CustomUserForm 
from django.contrib.auth import authenticate,login,logout
import json
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,"suba/index.html")

def collections(request):
    Catagory=catagory.objects.filter(status=0)
    return render(request,"suba/collections.html",{"Catagory":Catagory})

def collectionsview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        services=service.objects.filter(catagory__name=name)
        return render(request,'suba/layout/index.html',{"services":services,"catagory_name":name})
    else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')

def service_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
        if(service.objects.filter(name=pname,status=0)):
            services=service.objects.filter(name=pname,status=0).first()
            return render(request,'suba/layout/service_details.html',{"services":services})
        else:
            messages.error(request,"no such catagory found ")
            return redirect('collections')
    else:
        messages.error(request,"no such catagory found ")
        return redirect('collections')


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(User=request.user)
        return render(request,"suba/cart.html",{"cart":cart})
    else:
        return redirect("/")
def add_to_cart(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            service_id=data['pid']
            #print(request.user.id)
            service_status=service.objects.get(id=service_id)
            if service_status:
                if Cart.objects.filter(User=request.user.id,service_id=service_id):
                    return JsonResponse({'status':'Product Already in cart'},status=200)
                else:
                    Cart.objects.create(User=request.user,service_id=service_id)
                    return JsonResponse({'status':'Product Added to cart'},status=200)
        else:
            return JsonResponse({'status':'Login Added to cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            User=authenticate(request,username=name,password=pwd)
            if User is not None:
                login(request,User)
                messages.success(request,"loged in successfully")
                return redirect("/")
            else:
                messages.error(request,"invalid username & password")
                return redirect('/login')
        return render(request,"suba/login.html")  
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
    return redirect("/")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid ():
            form.save()
            messages.success(request,"registeration success you can login now...!")
            return redirect('/login')
    return render(request,"suba/register.html",{'form':form})

def about(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        body=request.POST.get('body')
        print(name,email,body)
        send_mail(
            'Caddcenter - chat ',
            name +" - "+body,
            'email',
            ['kandhakumar6996@gmail.com'],
            fail_silently=False,
        )
      
    return render(request,'suba/About.html')

def exterior(request):
    return render(request,"suba/our service/exterior.html")

def interior(request):
    return render(request,"suba/our service/interior.html")

def WheelAligment(request):
    return render(request,"suba/our service/WheelAligment.html")

def WaterWash(request):
    return render(request,"suba/our service/WaterWash.html")

def Enginework(request):
    return render(request,"suba/our service/Enginework.html")