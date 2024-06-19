from django.shortcuts import render
from .models import Teams

# Create your views here.
def home(request):
    #read/fetch data from admin panel- database postgres(pages_teams - table)
    teams = Teams.objects.all()
    context = {
        'teams':teams,
    }
    return render(request,'pages/home.html',context)


def about(request):
    teams = Teams.objects.all()
    context = {
        'teams':teams,
    }
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html')


def contact(request):
    return render(request,'pages/contact.html')