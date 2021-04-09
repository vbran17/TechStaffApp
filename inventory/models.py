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
    building = models.ForeignKey(Building, on_delete=models.RESTRICT, blank=True)
    address = models.CharField(max_length=40, blank=True)
    date = models.DateField(blank=True)
    in_use = models.BooleanField()

class History(models.Model):
    command = models.CharField(max_length=255, blank=True)
    execution_time = models.TimeField(blank=True)
    executor = models.EmailField(max_length=255, blank=True) 

class Equipment(models.Model):
    vttag = models.CharField(max_length=255, blank=True)
    building = models.ForeignKey(Building, blank=True, null=True, on_delete=models.CASCADE)
    room = models.CharField(max_length=15, blank=True)
    sdate = models.DateField(blank=True, null=True)
    manufacturer_model = models.CharField(max_length=255, blank=True)
    serial_number = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    classification =  models.CharField(max_length=255, blank=True)
    custodian = models.CharField(max_length=255, blank=True)
    porder = models.CharField(max_length=255, blank=True)
    pdate = models.CharField(max_length=255, blank=True)
    pvalue = models.CharField(max_length=255, blank=True)
    ip = models.ForeignKey(IP, on_delete=models.RESTRICT, blank=True)
    mac = models.CharField(max_length=255, blank=True)
    hostname = models.CharField(max_length=255, blank=True)
    surplus = models.SmallIntegerField(blank=True)
    history  = models.ForeignKey(History, on_delete=models.RESTRICT, blank=True)
    cnames = models.CharField(max_length=2048, blank=True)
    dept = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=128, blank=True)
    mailexhange = models.SmallIntegerField(blank=True)
    cstag = models.CharField(max_length=255, blank=True)

class Checkout(models.Model):
    contact = models.ForeignKey(PersonalID, on_delete=models.RESTRICT, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT, blank=True)
    checkoutdate = models.DateField(blank=True)





