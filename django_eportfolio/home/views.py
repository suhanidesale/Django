from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This is the home page")

def about(request):
    return HttpResponse("This is the about")
  
def projects(request):
    return HttpResponse("This is the projects")
  
def contact(request):
    return HttpResponse("This is the contact")
  