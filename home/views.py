from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import place,customer
# Create your views here.

def add(request):
    object=place.objects.all()
    obj=customer.objects.all()
    return render(request,'index.html',{'result':object,'cus':obj})
def login(request):
    if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
         auth.login(request,user)
         return redirect('/')
     else:
         messages.info(request,'invalid username or password')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=email)
        if password!=cpassword:
            messages.info(request,"password not matched")
        # elif User.objects.filter(username=username).exists():
        #     messages.ino(request,"username taken")
        else:
            user.save()
            return redirect('login')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def detail(request,movie_id):
    return HttpResponse("movie name is %s" %movie_id)