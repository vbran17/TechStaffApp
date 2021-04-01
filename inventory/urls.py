
from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'inventory'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('ipdashboard/', views.ipdash_view, name='ipdashboard'),
    path('searchresults/', views.searchresults_view, name='searchresults'),
    path('itemdetails/<int:item_id>', views.itemdetails_view, name='itemdetails'),
    path('addequipment/', views.addequipment_view, name='addequipment'),
    path('homeuseform/', views.homeuseform_view, name='homeuseform'),
    path('networkform/', views.networkform_view, name='networkform'),
    path('searchqueryform/', views.searchqueryform_view, name='searchqueryform'),
]