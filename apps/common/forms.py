from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)


class SubscriberFrom(forms.Form):
    email = forms.EmailField(required=True)
