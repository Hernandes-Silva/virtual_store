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
        self.fields['cpf'].widget.attrs = {'class': 'form-control', 'placeholder': "000.000.000-00"}
        self.fields['state'].widget.attrs = {'class': 'form-control' }
        self.fields['postal_code'].widget.attrs = {'class': 'form-control', 'placeholder': "00000-000"}
    
    input_class = "form-control mb-3"
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Completo",
                "class": input_class
            }
        )
    )
    email = forms.EmailField(
        widget=widgets.EmailInput(
            attrs = {
                "placeholder": "Email",
                "class": input_class
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TimeInput(
            attrs = {
                "placeholder": "Telefone",
                "class": input_class
            }
        )
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Cidade",
                "class": input_class
            }
        )
    )
    district = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Bairro",
                "class": input_class
            }
        )
    )
    street = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Rua",
                "class": input_class
            }
        )
    )
    complement = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Complemento",
                "class": input_class
            }
        )
    )
    number = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Numero",
                "class": input_class
            }
        )
    )
    