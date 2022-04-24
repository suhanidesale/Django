from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context

# Create your views here.
def home(request):
    # return HttpResponse("This is the home page")
    context = {'name': 'suhani', 'course': 'information technology'}
    return render(request , 'index.html')

def about(request):
    return HttpResponse("This is the about")
  
def projects(request):
    return HttpResponse("This is the projects")
  
def contact(request):
    if request.method=="POST":
        print("This is Post")
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name,email,desc)
    return HttpResponse("This is the contact")