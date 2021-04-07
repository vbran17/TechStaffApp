from django.db import models

# Create your models here.
class PersonalID(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)

class Building(models.Model):
    name = models.CharField(max_length=255)
    ipv6_prefix = models.CharField(max_length=255)

class IP(models.Model):
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)
    address = models.CharField(max_length=40)
    date = models.DateField()
    in_use = models.BooleanField()

class History(models.Model):
    command = models.CharField(max_length=255)
    execution_time = models.TimeField()
    executor = models.EmailField(max_length=255) 

class Equipment(models.Model):
    vttag = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.RESTRICT)
    room = models.CharField(max_length=15)
    sdate = models.DateField()
    manufacturer_model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    classification =  models.CharField(max_length=255)
    custodian = models.CharField(max_length=255)
    porder = models.CharField(max_length=255)
    pdate = models.CharField(max_length=255)
    pvalue = models.CharField(max_length=255)
    ip = models.ForeignKey(IP, on_delete=models.RESTRICT)
    mac = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    surplus = models.SmallIntegerField()
    history  = models.ForeignKey(History, on_delete=models.RESTRICT)
    cnames = models.CharField(max_length=2048)
    dept = models.CharField(max_length=10)
    status = models.CharField(max_length =128)
    mailexhange = models.SmallIntegerField()
    cstag = models.CharField(max_length=255)

class Checkout(models.Model):
    contact = models.ForeignKey(PersonalID, on_delete=models.RESTRICT)
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT)
    checkoutdate = models.DateField()





