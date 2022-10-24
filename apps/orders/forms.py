from django import forms

from .models import Order


class OrderCheckForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone_number', 'details', 'service']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone_number', 'details', 'service', 'attached', 'budget']
