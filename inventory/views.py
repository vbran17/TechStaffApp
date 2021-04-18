from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .serializers import IPSerializers
import csv
from django.http import HttpResponse, JsonResponse
from .forms import EquipmentForm, HostnameForm, BuildingForm, IPRangeForm
from django.core import serializers


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
        context["query"] = query
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


def admin_view(request):
    context = {}
    context["Users"] = User.objects.all()
    return render(request, 'inventory/admin.html', context)


def ipdash_view(request):
    building_objects = Building.objects.all()
    IP_objects = IP.objects.all()
    context = {
        'building_objects': building_objects,
        'IPs': IP_objects
    }
    return render(request, 'inventory/ip-dashboard.html', context)


class IPListing(ListAPIView):
    serializer_class = IPSerializers

    def get_queryset(self):
        ip_list = IP.objects.all()
        building = self.request.query_params.get('building', None)
        in_use = self.request.query_params.get('in_use', None)
        if building:
            ip_list = ip_list.filter(building__name=building)
        if in_use:
            ip_list = ip_list.filter(in_use=in_use)
        return ip_list


def IPDash(request):
    context = { }
    context['hostname_form'] = HostnameForm(request.POST or None)
    context['building_form'] = BuildingForm(request.POST or None)
    context['ip_range_form'] = IPRangeForm(request.POST or None)
    context['building_objects'] = Building.objects.all()

    if request.method == 'POST':
        if request.POST.get('buildingsubmit'):
            if context['building_form'].is_valid():
                context['building_form'].save()
        if request.POST.get('hostnamesubmit'):
            if context['hostname_form'].is_valid():
                context['hostname_form'].save()

    return render(request, "inventory/ip-dashboard.html", context)


def getBuilding(request):
    print("in building method")
    if request.method == "GET" and request.is_ajax():
        buildings = Building.objects.all().values_list('name').distinct()
        buildings = [i[0] for i in list(buildings)]
        data = {
            "buildings": buildings,
        }
        return JsonResponse(data, status=200)


def ipdash_view_filter(request):
    building_objects = Building.objects.all()
    IP_objects = IP.objects.all()
    context = {
        'building_objects': building_objects,
        'IPs': IP_objects
    }
    return render(request, 'inventory/ip-dashboard.html', context)


def itemdetails_view(request, item_id):
    # run a query to get all the info for the item_id
    id_item = int(item_id)
    temp = 'This is the ID %i' % (id_item)
    print(temp)

    item_list = Equipment.objects.filter(id=id_item)
    # if len(item_list) == 0:
    item = item_list[0]
    # print(item)
    executore = "carnold@vt.edu"
    history = History.objects.filter(executor=executore)
    print(history)
    return render(request, 'inventory/itemdetails.html', {'item': item, 'history': history})


def dns_view(request):
    items = Equipment.objects.all()
    size = len(items)
    results = 'Search returned %i items(s)' % (size)
    value = 0

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dns.csv"'
    writer = csv.writer(response)
    writer.writerow([results])
    writer.writerow(['CS Tag', 'Custodian', 'Hostname',
                    'Location', 'Manufacturer-Model', 'VT Tag'])
    for i in items:
        if i.purchase_value != "":
            value = value + int(i.purchase_value)
        writer.writerow([i.cs_tag, i.custodian, i.hostname.hostname, i.building.name, i.manufacturer_model, i.vt_tag])
    total = 'Total value: $%i' % (value)
    print(results)
    print(total)

    writer.writerow([total])
    return response


def addequipment_view(request):
    form = EquipmentForm(request.POST or None)
    '''
    if request.method == "GET":
        print(form.cleaned_data["hostname"])
        return JsonResponse({"abc": 123})
    '''
    if form.is_valid():
        form.save()
        return redirect('/home')
    return render(request, 'inventory/addequipment.html', {'form':form})

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
                equipments = Equipment.objects.filter(
                    Q(vttag__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'cstag':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(cstag__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'serial_number':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(serial_number__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'manufacturer_model':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(manufacturer_model__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'custodian':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(custodian__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'hostname':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(hostname__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'building':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(building__icontains=q)).distinct()
                for equipment in equipments:
                    queryset.append(equipment)
        elif filter == 'ip':
            for q in queries:
                equipments = Equipment.objects.filter(
                    Q(ip__icontains=q)).distinct()
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
