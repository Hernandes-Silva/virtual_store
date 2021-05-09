from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from products.models import Department, Category, Product
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
class ListCategoryView(LoginRequiredMixin, ListView):
    model = Category
    login_url = "/admin/"
    template_name = "category_list.html"
    context_object_name = 'categories'
class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = "category_create.html"
    success_url = reverse_lazy('category_list')
class ListProductView(LoginRequiredMixin, ListView):
    model = Product
    login_url = "/admin/"
    template_name = "home.html"
    context_object_name = 'products'
class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    template_name = "product_create.html"
    success_url = reverse_lazy('home')

