from django import forms
from django.forms import ModelForm
from .models import Equipment, Building, Hostname


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['dept', 'status', 'vt_tag', 'cs_tag', 'serial_number', 'manufacturer_model', 'classification', 'description',
                    'custodian', 'purchase_order', 'acquisition_date', 'purchase_date',
                    'purchase_value', 'building', 'room', 'hostname', 'notes']
        CLASSIFICTATIONS = (('', '---------'),('laptop', 'Laptop'), ('desktop', 'Desktop'))
        CUSTODIANS = (('', '--------------------'),('rich', 'Richard Charles'), ('chris', 'Chris Arnold'), ('mike', 'Micheal Davis'))
        widgets = {'classification': forms.Select(choices=CLASSIFICTATIONS), 
                    'custodian': forms.Select(choices=CUSTODIANS), 
                    'notes': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'description': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'pdate': forms.DateInput(attrs={'data-target': '.datepicker'})}


class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'ipv6_prefix']


class HostnameForm(ModelForm):
    class Meta:
        model = Hostname
        fields = ['hostname', 'ipv4', 'ipv6', 'aliases']

#for IP Form?
class IPRangeForm(forms.Form):
    ip_range = forms.CharField(label='IP Range', max_length=256)




        