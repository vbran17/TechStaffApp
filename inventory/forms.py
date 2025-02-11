from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.validators import RegexValidator


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['dept', 'status', 'vt_tag', 'cs_tag', 'serial_number', 'manufacturer_model', 'classification', 'description',
                    'custodian', 'purchase_order', 'acquisition_date', 'purchase_date',
                    'purchase_value', 'building', 'room', 'hostname', 'notes']
        CLASSIFICTATIONS = (('', '---------'),('laptop', 'Laptop'), ('desktop', 'Desktop'))
        
        STATUSES = (('', '--------'), ('in_use', 'In use'), ('in_storage', 'In storage'), ('on_loan', 'On loan'),
                    ('damaged', 'Damaged'), ('missing', 'Missing'), ('surplused', 'Surplused'), ('transferred', 'Transferred'),
                    ('written_off', 'Written off'), ('orphaned', 'Orphaned'))
        CUSTODIANS = (('', '--------------------'),('rich', 'Richard Charles'), ('chris', 'Chris Arnold'), ('mike', 'Micheal Davis'))
        
        widgets = {
                    'status': forms.Select(choices=STATUSES, attrs={'class': 'form-select'}),
                    'classification': forms.Select(choices=CLASSIFICTATIONS, attrs={'class': 'form-select'}), 
                    'custodian': forms.Select(choices=CUSTODIANS), 
                    'notes': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'description': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'pdate': forms.DateInput(attrs={'data-target': '.datepicker'}),
                    'vt_tag': forms.TextInput(attrs={'class': 'form-control'}),
                    'cs_tag': forms.TextInput(attrs={'class': 'form-control'}),
                    'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
                    'manufacturer_model': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.Textarea(attrs={'class': 'form-control'}),
                    'purchase_order': forms.TextInput(attrs={'class': 'form-control'}),
                    'purchase_value': forms.NumberInput(attrs={'class': 'form-control'}),
                    'building': forms.Select(attrs={'class': 'form-select'}),
                    'room': forms.TextInput(attrs={'class': 'form-control'}),
                    'notes': forms.Textarea(attrs={'class': 'form-control'}),}



class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'ipv6_prefix']

class HostnameForm(ModelForm):
    ipv4 = forms.ModelChoiceField(queryset=IP.objects.filter(in_use=False, ip_type="IPv4"))
    class Meta:
        model = Hostname
        fields = ['hostname', 'building', 'ipv4', 'ipv6', 'aliases']

#for IP Form?
class IPRangeForm(forms.Form):
    ip_range_begin = forms.CharField(label='IP or IP Range Start', max_length=256, validators=[
        RegexValidator('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', message="Must be valid IPv4 address, 0-255.0-255.0-255.0-255 acceptable")])
    ip_range_end = forms.CharField(label='IP Range End', max_length=256, required=False, validators=[
        RegexValidator('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', message="Must be valid IPv4 address, 0-255.0-255.0-255.0-255 acceptable")])
    building = forms.ModelChoiceField(queryset=Building.objects.all(), empty_label="--Select a building--")

#used in conjuction with Hostname Form
class IPv6Form(forms.Form):
    genipv6 = forms.CharField(label='IP or IP Range Start', max_length=256)

class InventoryUserForm(ModelForm):
    class Meta:
        model = InventoryUser
        exclude = ['user']
        fields = ['phone_number', 'pid']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pid': forms.TextInput(attrs={'class': 'form-control'})
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),            
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
