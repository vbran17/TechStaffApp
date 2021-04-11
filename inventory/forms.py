from django import forms
from django.forms import ModelForm
from .models import Equipment

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        CLASSIFICTATIONS = (('', '---------'),('laptop', 'Laptop'), ('desktop', 'Desktop'))
        CUSTODIANS = (('', '--------------------'),('rich', 'Richard Charles'), ('chris', 'Chris Arnold'), ('mike', 'Micheal Davis'))
        widgets = {'classification': forms.Select(choices=CLASSIFICTATIONS), 
                    'custodian': forms.Select(choices=CUSTODIANS), 
                    'notes': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'description': forms.Textarea(attrs={'cols': 40, 'rows': 3}), 
                    'pdate': forms.DateInput(attrs={'data-target': '.datepicker'})}
        exclude = ['history']