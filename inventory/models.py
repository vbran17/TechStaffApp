from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.

class InventoryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone number")
    pid = models.CharField(max_length=255, blank=True, null=True, verbose_name="PID")
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Building(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Building")
    ipv6_prefix = models.CharField(max_length=255, blank=True, null=True, verbose_name="IPv6 prefix")
    def __str__(self):
        return self.name

class IP(models.Model):
    IPv4='IPv4'
    IPv6='IPv6'
    ip_types = [
        (IPv4, "IPv4"),
        (IPv6, "IPv6"),
    ]
    building = models.ForeignKey(Building, on_delete=models.RESTRICT, blank=True, verbose_name="Building")
    ip_type = models.CharField(choices=ip_types, max_length=5, default=IPv4, verbose_name="IP type")
    address = models.CharField(max_length=40, blank=True, verbose_name="Address")
    date = models.DateField(auto_now_add=True, blank=True, verbose_name="Date")
    in_use = models.BooleanField(verbose_name="In use")
    def __str__(self):
        return self.address


class Hostname(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="Hostname")
    building = models.ForeignKey(Building, on_delete=models.RESTRICT, blank=True, verbose_name="Building")
    aliases = models.CharField(max_length=255, blank=True, verbose_name="Aliases")
    ipv4 = models.ForeignKey(IP, on_delete=models.SET_NULL, null=True, blank=True, related_name="HostnameIPv4", verbose_name="IPv4")
    ipv6 = models.ForeignKey(IP, on_delete=models.SET_NULL, null=True, blank=True, related_name="HostnameIPv6", verbose_name="IPv6")
    in_use = models.BooleanField(verbose_name="In Use")
    def __str__(self):
        return self.hostname

class Equipment(models.Model):
    vt_tag = models.CharField(max_length=255, blank=True, null=True, verbose_name="VT tag")
    building = models.ForeignKey(Building, blank=True, null=True, on_delete=models.RESTRICT, verbose_name="Building")
    room = models.CharField(max_length=15, blank=True, null=True, verbose_name="Room")
    manufacturer_model = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manufacturer/Model")
    serial_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Serial number")
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Description")
    classification =  models.CharField(max_length=255, blank=True, null=True, verbose_name="Classification")
    custodian = models.CharField(max_length=255, blank=True, null=True, verbose_name="Custodian")
    purchase_order = models.CharField(max_length=255, blank=True, null=True, verbose_name="Purchase order")
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Purchase date")
    purchase_value = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Purchase value")
    acquisition_date = models.DateField(blank=True, null=True, verbose_name="Acquisition date")
    hostname = models.ForeignKey(Hostname, on_delete=models.RESTRICT, blank=True, null=True, related_name="Hostname", verbose_name="Hostname")
    dept = models.CharField(max_length=10, blank=True, verbose_name="Department")
    status = models.CharField(max_length=128, blank=True, verbose_name="Status")
    mail_exchange = models.ForeignKey(Hostname, on_delete=models.RESTRICT, blank=True, null=True, related_name="MailExchangeHostname", verbose_name="Mail exchange")
    #have to change mail exchange to hostname 
    cs_tag = models.CharField(max_length=255, blank=True, null=True, verbose_name="CS tag")
    notes = models.CharField(max_length=10000, blank=True, null=True, verbose_name="Notes")

class Checkout(models.Model):
    contact = models.ForeignKey(InventoryUser, on_delete=models.RESTRICT, blank=True, verbose_name="Contact")
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT, blank=True, verbose_name="Equipment")
    checkoutdate = models.DateField(blank=True, auto_now_add=True, verbose_name="Checkout date")

class History(models.Model):
    command = models.CharField(max_length=255, blank=True, verbose_name="Command")
    execution_time = models.TimeField(auto_now_add=True, blank=True, verbose_name="Execution time")
    executor = models.EmailField(max_length=255, blank=True, verbose_name="Executor") 
    equipment = models.ForeignKey(Equipment, on_delete=models.RESTRICT, blank=True, verbose_name="Equipment")
