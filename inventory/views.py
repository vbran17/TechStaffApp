from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from .models import Equipment
from django.http import JsonResponse
import json



# Create your views here.
def home_view(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        equipments = Equipment.filter(manufacturer_model__starts_with=search_str)
        data = equipments.values()

        return JsonResponse(list(data), safe=False)


    return render(request, 'inventory/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    # redirect to a success page.
        

def ipdash_view(request):
    return render(request, 'events/ip-dashboard.html')

def searchresults_view(request):
    return render(request, 'events/index.html')

def itemdetails_view(request):
    return render(request, 'events/index.html')
 
def addequipment_view(request):
    return render(request, 'events/index.html')

def homeuseform_view(request):
    return render(request, 'events/index.html')
 
def networkform_view(request):
    return render(request, 'events/index.html')

def searchqueryform_view(request):
    return render(request, 'events/index.html')
