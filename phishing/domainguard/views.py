from django.shortcuts import render, HttpResponse
from .models import submittedURLs

def home(request):
    return render(request,"home.html")

def model(request):
    return render(request,"model.html")

def URLs(request):
    items = submittedURLs.objects.all()
    return render(request,"urls.html", {"URLs":items})
