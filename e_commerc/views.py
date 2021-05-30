
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from products.models import Department, Category
# Create your views here.
def CategoryView(request, department_slug, slug):
    department = get_object_or_404(Department, slug = department_slug)
    category = get_object_or_404(Category, slug = slug)
    products = category.products.all()
    return render(request, 'ecommerc_category.html', {'products': products})
class DepartmentView(DetailView):
    model = Department
    template_name = "ecommerc_departments.html"
    context_object_name = "department"
    
