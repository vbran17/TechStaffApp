from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Equipment)
admin.site.register(IP)
admin.site.register(History)
admin.site.register(Checkout)
admin.site.register(Building)
admin.site.register(Hostname)
admin.site.register(PersonalID)