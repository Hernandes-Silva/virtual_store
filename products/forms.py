from django import forms
from django.forms import widgets
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
        self.fields['price'].widget.attrs = {'class': 'form-control','step': '0.01'}
        self.fields['image'].widget.attrs = {'class': 'form-control', 'required':'required'}


class TechnicalInformationForm(forms.ModelForm):
    class Meta:
        model = TechnicalInformation
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(TechnicalInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}