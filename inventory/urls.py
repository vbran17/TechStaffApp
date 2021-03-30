
from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('ipdashboard/', views.ipdash, name='ipdashboard'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('itemdetails/<int:item_id>', views.itemdetails, name='itemdetails'),
    path('addequipment/', views.addequipment, name='addequipment'),
    path('homeuseform/', views.homeuseform, name='homeuseform'),
    path('networkform/', views.networkform, name='networkform'),
    path('searchqueryform/', views.searchqueryform, name='searchqueryform'),
]