from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ContactMessage, PurchaseRequest, PremiumUser

def home(request):
    return render(request, 'core/index.html')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/')

        user = User.objects.create_user(username=username, email=email, password=password)
        PremiumUser.objects.create(user=user)
        messages.success(request, "Registration Successful")
        return redirect('/')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful")
        else:
            messages.error(request, "Invalid Credentials")
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def contact_submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Message Sent Successfully")
        return redirect('/')

def buy_plan(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        plan = request.POST['plan']

        PurchaseRequest.objects.create(name=name, email=email, phone=phone, plan=plan)
        messages.success(request, "Purchase Request Submitted")
        return redirect('/')