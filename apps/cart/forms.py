from django import forms
from .models import Billing


class BillingForm(forms.ModelForm):

    class Meta:
        model = Billing
        widjets = {
            'First_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your name: '
            }),
            'Last_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your last name: '
            }),
            'State': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your state name: '
            }),
            'Phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone: '
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'Street_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your street name: '
            }),
            'City': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your city name: '
            }),
            'Zip': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your zip code: '
            })
        }
        fields = ['First_name', 'Last_Name', 'State', 'Street_address', 'City', 'Zip', 'phone', 'email_address']

