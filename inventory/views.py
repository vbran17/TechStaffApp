from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .serializers import IPSerializers, BuildingSerializers, HostnameSerializers
import csv

from django.http import HttpResponse
from .forms import EquipmentForm

import re
from django import forms
from django.http import HttpResponse, JsonResponse
from .forms import EquipmentForm, HostnameForm, BuildingForm, IPRangeForm
from django.core import serializers
from django.contrib import messages


from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import *
from django.core import serializers
from django.contrib import messages
from django.forms import formset_factory




# Create your views here.
def home_view(request):
    # Handles search query
    context = {}
    #context['options'] = {"VT Tag": "vttag", "CS Tag": "cstag", "Serial Number": "serial_number",
    #                      "Manufacturer": "manufacturer_model", "Custodian": "custodian", "Hostname": "hostname",
    #                      "Building": "building", "IP": "ip"}
    #query = ""
    #selected_option = ""
    if request.method == "GET":
        query = request.GET.get('search')
        selected_option = request.GET.get('search_options')
        context["query"] = query
        context["selected_option"] = selected_option
    context['equipments'] = Equipment.objects.all()
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

def gen_ipv6(request, b_name, item_id):
    building = Building.objects.filter(id=b_name)
    if len(building) == 0:
        messages.info(request, "No Building prefix found")
    else:
        ipv6 = IP()
        ipv6.building = building[0]
        ipv6.ip_type = "I6"
        ipv6.in_use = True
        address = building[0].ipv6_prefix + "::1111:1111:1113"
        print(address)
        ipv6.address = address
        ipv6.save()
        equip = Equipment.objects.get(id=item_id)
        if equip.hostname:
            print("Hostname specified %s" % equip.hostname.hostname)
            print(equip.hostname.ipv6.address)
            equip.hostname.ipv6 = ipv6 
            #equip.hostname.ipv6.save()
            equip.hostname.save()
            print(equip.hostname.ipv6.address)
            # create new command stamp
            newCommand = History()
            newCommand.command = "IPv6 created"
            executor = '%s@vt.edu' % equip.custodian
            print(executor)
            newCommand.executor = executor
            newCommand.equipment = equip
            newCommand.save()
        else:
            print("No hostname specified")
            messages.info(request, "No hostname specified")
    print("Ypu are in IPv6")
    
    return redirect('/itemdetails/%i/' % item_id)
def apply_changes(request, item_id):
    equip = Equipment.objects.get(id=item_id)
    CSTag = request.POST.get('cstag','').strip()
    Notes = request.POST.get('notes','').strip()
    VTTag = request.POST.get('vttag','').strip()
    Description = request.POST.get('desc','').strip()
    HostedName = request.POST.get('host', '').strip()
    Alias = request.POST.get('alias', '').strip()
    if equip:
        equip.notes = Notes
        equip.cs_tag = CSTag
        equip.vt_tag = VTTag
        equip.description = Description
        equip.save()
        print('New Notes: ')
        print(Notes)
        print('CSTag is: ')
        print(CSTag)
        print('VTTag is: ')
        print(VTTag)
        print('New description is: ')
        print(VTTag)
        host = Hostname.objects.filter(hostname=HostedName, building=equip.building, in_use=False)
        if len(host) > 0:
            print(host[0].building.name)
            if equip.hostname:
                if equip.hostname != host[0]:
                    equip.hostname.in_use = False
                    equip.hostname = host[0]
                    equip.hostname.save()
                    messages.success(request, "Hostname Reassigned!")
                else:
                    messages.success(request, "Hostname currently in use")
            else:
                equip.hostname = host[0]
                equip.hostname.in_use = True
                equip.hostname.save()
                messages.success(request, "Hostname Assigned!")
        else:
            # Needs to have a hostname created in the hostname for this to work properly
            if equip.hostname.hostname == HostedName:
                # messages.info(request, "Hostname in use")
                print("Lol")
            else:
                messages.info(request, "Hostname not found under building %s or it is being used" % equip.building.name)
        if equip.hostname:
            if equip.hostname.aliases != Alias:
                equip.hostname.aliases = Alias
                equip.hostname.save()
                messages.info(request, "Alias Added!")
            else: 
                print("Lol")
        else:
            messages.info(request, "Cannot assign aliases to empty hostname!")
    else:
        messages.info(request, "Equipment not found")
        print("Equpiment not found")
    return redirect('/itemdetails/%i/' % item_id)

def gen_ipv4(request, b_name, item_id):
    ipv4 = IP.objects.filter(building=b_name,in_use=False, ip_type='I4')
    if len(ipv4) > 0:
        freeIP = ipv4[0]
        print(freeIP.address)
        freeIP.in_use = True
        print(freeIP.in_use)
        # map it to the equipment 
        equip = Equipment.objects.get(id=item_id)
        print(equip.hostname.id)
        if equip.hostname.ipv4:
            print("IP type")
            print(equip.hostname.ipv4.ip_type)
            # free current ip, set in_use to false
            equip.hostname.ipv4.in_use = False
            equip.hostname.ipv4 = freeIP
            #equip.hostname.ipv4.address = freeIP.address
            equip.hostname.ipv4.save()
            equip.hostname.save()
            print("not null")
        else:
            equip.hostname.ipv4 = freeIP
            equip.save()
        print(equip.hostname.ipv4.address)
        # update history
        newCommand = History()
        newCommand.command = "IPv4 created"
        executor = '%s@vt.edu' % equip.custodian
        print(executor)
        newCommand.executor = executor
        newCommand.equipment = equip
        newCommand.save()
    else:
        messages.info(request, "No Free IP found for building range")
        print("No free IP found")
    
    # change the in_use form
    return redirect('/itemdetails/%i/' % item_id)

def admin_view(request):
    context = {}
    context["Users"] = User.objects.all()
    context["UserForm"] = UserForm(request.POST or None)
    context["InventoryUserForm"] = InventoryUserForm(request.POST or None)
    #UserFormset = formset_factory(context["UserForm"])
    #InventoryUserFormset = formset_factory(context["InventoryUserForm"])
    print(request.method)
    print(request)
    if request.method == "POST":
        if request.POST.get('userID'):
            User.objects.filter(id=request.POST.get('userID')).delete()
            print("|"+request.POST.get('userID')+"|")
            print("gets heres")
            #print(UserFormset.errors)
            print(context["InventoryUserForm"].errors)
            print(context["UserForm"].errors)
        elif context["UserForm"].is_valid() and context["InventoryUserForm"].is_valid():
            user = context["UserForm"].save()
            inventory_user = context["InventoryUserForm"].save(commit=False)
            inventory_user.user = user
            inventory_user.save()
            print("gets heres")

    return render(request, 'inventory/admin.html', context)

def IPDash(request):
    context = { }
    context['hostname_form'] = HostnameForm(request.POST or None)
    context['building_form'] = BuildingForm(request.POST or None)
    context['ip_range_form'] = IPRangeForm(request.POST or None)
    context['building_objects'] = Building.objects.all()
    context['IPS'] = IP.objects.all()
    context['Hosts'] = Hostname.objects.all()

    if request.method == 'POST':
        if request.POST.get('buildingsubmit'):
            if context['building_form'].is_valid():
                context['building_form'].save()
        if request.POST.get('genipv6'):
            print("generate ipv6")
        if request.POST.get('hostnamesubmit'):
            
            if context['hostname_form'].is_valid():
                context['hostname_form'].save()

        if request.POST.get('iprangesubmit'):
            if context['ip_range_form'].is_valid():
                selected_building = context['ip_range_form'].cleaned_data['building']
                ip_or_range_start = context['ip_range_form'].cleaned_data['ip_range_begin']

                if context['ip_range_form'].cleaned_data['ip_range_end']:
                    sets = ip_or_range_start.split(".")
                    b_sets = list(map(int,sets))
                    e_sets = list(map(int,(context['ip_range_form'].cleaned_data['ip_range_end']).split(".")))
                    fixed = sets[0] + sets[1] + sets[2]
                    fixed = ".".join(sets[:3]) + "."
                    if b_sets[:3] == e_sets[:3] and e_sets[3] >= b_sets[3]:
                        ip_count = 0
                        missed = []
                        for i in range(b_sets[3], e_sets[3] + 1):
                            address = fixed + str(i)
                            if IP.objects.filter(address=address).count() > 0:
                                missed.append(str(i))
                            else:
                                IP.objects.create(
                                    building=selected_building,
                                    address=address,
                                    in_use=False)  
                                ip_count = ip_count + 1
                        if ip_count > 0:
                            messages.add_message(request, messages.SUCCESS, str(ip_count) + " IPv4(s) submitted!")
                        if len(missed) > 0:
                            duplicate_sets =  ",".join(missed)
                            messages.add_message(request, messages.ERROR, "Duplicates found: " + fixed + " (" + duplicate_sets + ")")
                    else:
                        messages.add_message(request, messages.ERROR, "First three 8-bit numbers should be equal for range")
                else:
                    if IP.objects.filter(address=ip_or_range_start).count() > 0:
                        messages.add_message(request, messages.ERROR, "Address: " + ip_or_range_start + " already in DB")
                    else:
                        IP.objects.create(
                            building=selected_building,
                            address=ip_or_range_start,
                            in_use=False)
                        messages.add_message(request, messages.SUCCESS, "IPv4 submitted!")
                
                return HttpResponseRedirect("/ipdashboard")
            else:
                messages.add_message(request, messages.WARNING, context['ip_range_form'].errors)
                    
                    



        if request.POST.get('IP_ID'):
            value = request.POST['IP_ID']
            IP.objects.get(id=value).delete()

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
    history = History.objects.filter(equipment=id_item)
    print(history)
    return render(request, 'inventory/itemdetails.html', {'item': item, 'history': history})
 
def item_delete(request, item_id):
    print(request.path)
    request.path = "/home/"
    request.path_info = "/home/"
    print(request.path_info)
    return redirect('/home/')


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
