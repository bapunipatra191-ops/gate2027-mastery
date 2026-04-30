from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, "This email is already subscribed!")
            else:
                Subscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing! We'll keep you updated on GATE 2027.")
        return redirect('index')
    return render(request, "core/index.html")
