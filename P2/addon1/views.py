from django.shortcuts import render

def home(request):
    return render (request, "addon1/home.html")
# Create your views here.
