from django.db import models

# Create your models here.
class PersonalID(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)

class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ipv6_prefix = models.CharField(max_length=255, blank=True, null=True)

class IP(models.Model):
    IPv4='I4'
    IPv6='I6'
    ip_types = [
        (IPv4, "IPv4"),
        (IPv6, "IPv6"),
    ]
    building = models.ForeignKey(Building, on_delete=models.RESTRICT, blank=True)
    ip_type = models.CharField(choices=ip_types, max_length=2, default=IPv4)
    address = models.CharField(max_length=40, blank=True)
    date = models.DateField(blank=True)
    in_use = models.BooleanField()

class Hostname(models.Model):
    hostname = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.RESTRICT, blank=True)
    aliases = models.CharField(max_length=255, blank=True)
    ipv4 = models.ForeignKey(IP, on_delete=models.RESTRICT, blank=True, related_name="HostnameIPv4")
    ipv6 = models.ForeignKey(IP, on_delete=models.RESTRICT, blank=True, related_name="HostnameIPv6")

class Equipment(models.Model):
    vt_tag = models.CharField(max_length=255, blank=True)
    building = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)
    room = models.CharField(max_length=15, blank=True)
    manufacturer_model = models.CharField(max_length=255, blank=True)
    serial_number = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    classification =  models.CharField(max_length=255, blank=True)
    custodian = models.CharField(max_length=255, blank=True)
    purchase_order = models.CharField(max_length=255, blank=True)
    purchase_date = models.DateField(blank=True)
    purchase_value = models.CharField(max_length=255, blank=True)
    acquisition_date = models.DateField(blank=True)
    hostname = models.ForeignKey(Hostname, on_delete=models.RESTRICT, blank=True)
    dept = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=128, blank=True)
    cs_tag = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=10000, blank=True)

class Checkout(models.Model):
    contact = models.ForeignKey(PersonalID, on_delete=models.RESTRICT, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT, blank=True)
    checkoutdate = models.DateField(blank=True)

class History(models.Model):
    command = models.CharField(max_length=255, blank=True)
    execution_time = models.TimeField(blank=True)
    executor = models.EmailField(max_length=255, blank=True) 
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT, blank=True)
    





