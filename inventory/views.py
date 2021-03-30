from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'inventory/base.html')

def login(request):
    return render(request, 'events/index.html')

def ipdash(request):
    return render(request, 'events/index.html')

def searchresults(request):
    return render(request, 'events/index.html')

def itemdetails(request):
    return render(request, 'events/index.html')
 
def addequipment(request):
    return render(request, 'events/index.html')

def homeuseform(request):
    return render(request, 'events/index.html')
 
def networkform(request):
    return render(request, 'events/index.html')

def searchqueryform(request):
    return render(request, 'events/index.html')
