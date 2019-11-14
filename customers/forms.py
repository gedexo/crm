from django import forms
from django.forms.widgets import TextInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
from customers.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['auto_id','creator','updater','is_deleted']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control','placeholder' : 'Name'}),
            'email': TextInput(attrs={'class': 'required email form-control','placeholder' : 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control','placeholder' : 'Phone'}),
            'address': Textarea(attrs={'class': 'required form-control','placeholder' : 'Address'}),
        }
        error_messages = {
            'name' : {
                'required' : _("Name field is required."),
            },
            'email' : {
                'required' : _("Email field is required."),
            },
            'phone' : {
                'required' : _("Phone field is required."),
            },
            'address' : {
                'required' : _("Addess field is required."),
            },
        }