from django import forms
from django.forms import widgets
from .models import Order
from localflavor.br.models import BRCPFField, BRPostalCodeField, BRStateField
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'cpf',
            'email',
            'phone',
            'postal_code',
            'state',
            'city',
            'district',
            'street',
            'complement',
            'number',
        ]
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs = {'class': 'form-control'}
    
    field_classes = {
        'phone': 'form-control'
    }
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Completo",
                "class": ""
            }
        )
    )
    
    