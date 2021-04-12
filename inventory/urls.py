
from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'inventory'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('home/DNS_Form/', views.dns_view, name='dns'),
    path('admin/auth/admin_view', views.admin_view, name='admin'),
    path('ipdashboard/', views.ipdash_view, name='ipdashboard'),
    path('itemdetails/<int:item_id>/', views.itemdetails_view, name='itemdetails'),
    path('addequipment/', views.addequipment_view, name='addequipment'),
    path('homeuseform/', views.homeuseform_view, name='homeuseform'),
    path('networkform/', views.networkform_view, name='networkform'),
    path('searchqueryform/', views.searchqueryform_view, name='searchqueryform'),
]
