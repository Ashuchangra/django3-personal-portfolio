from django.shortcuts import render
from .models import Project
from .models import Dumps

def home(request):
    projects=Project.objects.all()
    dumps=Dumps.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects,'dumps':dumps})
