
from django.urls import path
from . import views
from django.conf.urls import include
from django.views.generic.base import RedirectView

app_name = 'inventory'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', RedirectView.as_view(url='http://localhost:8000/login/'), name='login-redirect'),
    path('home/', views.home_view, name='home'),
    path('home/DNS_Form/', views.dns_view, name='dns'),
    path('admin/auth/admin_view', views.admin_view, name='admin'),
    path('ipdashboard/', views.IPDash, name="ipdashboard"),
    path('ajax/buildings/', views.getBuilding, name = 'get_building'),
    path('itemdetails/<int:item_id>/', views.itemdetails_view, name='itemdetails'),
    path('itemdetails/<int:item_id>/delete/', views.item_delete, name='item_delete'),
    path('addequipment/', views.addequipment_view, name='addequipment'),
    path('homeuseform/', views.homeuseform_view, name='homeuseform'),
    path('networkform/', views.networkform_view, name='networkform'),
    path('searchqueryform/', views.searchqueryform_view, name='searchqueryform'),
    path('IPv4/<int:b_name>/<int:item_id>', views.gen_ipv4, name='ipv4'),
    path('IPv6/<int:b_name>/<int:item_id>', views.gen_ipv6, name='ipv6'),
    path('itemdetails/<int:item_id>/apply_changes/', views.apply_changes, name='apply_changes'),

]
