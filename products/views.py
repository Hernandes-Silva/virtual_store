from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from products.models import Department
from django.urls import reverse_lazy

# Create your views here.
class ListDepartmentView(LoginRequiredMixin, ListView):
    model = Department
    login_url = '/admin/'
    template_name = 'department_list.html'
    context_object_name = 'departments'
class CreateDepartmentView(LoginRequiredMixin, CreateView):
    model = Department
    fields = "__all__"
    template_name= "department_create.html"
    success_url = reverse_lazy('department_list')