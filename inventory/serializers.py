from rest_framework import serializers
from .models import IP, Building, Hostname




class BuildingSerializers(serializers.ModelSerializer):
	class Meta:
	    model = Building
	    fields = '__all__'

class IPSerializers(serializers.ModelSerializer):
	building = BuildingSerializers()
	class Meta:
	    model = IP
	    fields = ('id', 'building', 'ip_type', 'address', "date", "in_use")

class HostnameSerializers(serializers.ModelSerializer):
	ipv4 = IPSerializers()
	ipv6 = IPSerializers()
	class Meta:
	    model = Hostname
	    fields = ['hostname', 'building', 'aliases', 'ipv4', 'ipv6', 'in_use']
