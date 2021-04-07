from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from .models import Equipment
from django.db.models import Q



# Create your views here.
def home_view(request):
    # Handles search query
    context = {}
    context['options'] = {"VT Tag": "vttag", "CS Tag": "cstag", "Serial Number": "serial_number",
                            "Manufacturer": "manufacturer_model", "Custodian": "custodian", "Hostname": "hostname",
                            "Building": "building", "IP": "ip"}
    query = ""
    selected_option = ""
    if request.method == "GET":
        query = request.GET.get('search')
        selected_option = request.GET.get('search_options')
        context["query"] =  query
        context["selected_option"] = selected_option
    context['equipments'] = get_equipment_queryset(query, selected_option)
    return render(request, 'inventory/home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
    return render(request, 'inventory/login.html')

def logout_view(request):
    logout(request)
    # redirect to a success page.


def ipdash_view(request):
    return render(request, 'inventory/ip-dashboard.html')

def itemdetails_view(request, item_id):
    #run a query to get all the info for the item_id 
    return render(request, 'inventory/itemdetails.html')
 
def addequipment_view(request):
    return render(request, 'inventory/addequipment.html')

def homeuseform_view(request):
    return render(request, 'events/index.html')

def networkform_view(request):
    return render(request, 'events/index.html')

def searchqueryform_view(request):
    return render(request, 'events/index.html')

def get_equipment_queryset(query=None, filter=None):
    if query:
        queryset = []
        queries = query.split(" ")
        if filter == 'vttag':
            for q in queries:
                equipments = Equipment.objects.filter(Q(vttag__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'cstag':
            for q in queries:
                equipments = Equipment.objects.filter(Q(cstag__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'serial_number':
            for q in queries:
                equipments = Equipment.objects.filter(Q(serial_number__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'manufacturer_model':
            for q in queries:
                equipments = Equipment.objects.filter(Q(manufacturer_model__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'custodian': 
            for q in queries:
                equipments = Equipment.objects.filter(Q(custodian__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'hostname':
            for q in queries:
                equipments = Equipment.objects.filter(Q(hostname__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'building':
            for q in queries:
                equipments = Equipment.objects.filter(Q(building__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        elif filter == 'ip':
            for q in queries:
                equipments = Equipment.objects.filter(Q(ip__icontains=q)).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        else:
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(vttag__icontains=q) |
                    Q(cstag__icontains=q) |
                    Q(serial_number__icontains=q) |
                    Q(manufacturer_model__icontains=q) |
                    Q(custodian__icontains=q) |
                    Q(hostname__icontains=q) |
                    Q(building__icontains=q) |
                    Q(ip__icontains=q)
                ).distinct()
                for equipment in equipments: 
                    queryset.append(equipment)
        return list(set(queryset))
    else:
        return Equipment.objects.all()
