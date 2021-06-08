from django import forms
from django.forms import widgets
from .models import Card
class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {'class': 'form-control',}
        
    
    input_class = "form-control mb-3"

    link = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Completo",
                "class": input_class
            }
        )
    )

    descricion = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                "placeholder": "Descrição",
                "class": input_class
            }
        )
    )
    price = forms.FloatField(
        widget=forms.NumberInput(
            attrs = {
                "step":"0.01",
                "placeholder": "Preço",
                "class": input_class
            }
        )
    )