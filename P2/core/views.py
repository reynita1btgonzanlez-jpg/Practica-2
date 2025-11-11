from django.shortcuts import render

def index(request):
    retrurn render(request, "core/index.html")
    
# Create your views here.
