from rest_framework import serializers
from .models import IP

class IPSerializers(serializers.ModelSerializer):
	class Meta:
	    model = IP
	    fields = ('id', 'building', 'ip_type', 'address', "date", "in_use")