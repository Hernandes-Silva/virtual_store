

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.views.generic.base import TemplateView
from products.models import Department, Category, Product
from e_commerc.models import Card
from e_commerc.forms import CardForm
from django.urls import reverse_lazy
from rolepermissions.mixins import HasPermissionsMixin
# Create your views here.
def template_base(request):
    base_departments = Department.objects.all()
    return {'base_departments': base_departments}

def CategoryView(request, department_slug, slug):
    department = get_object_or_404(Department, slug = department_slug)
    category = get_object_or_404(Category, slug = slug)
    products = category.products.all()
    return render(request, 'ecommerc_category.html', {'products': products, 'department':department })

def searchView(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        products = Product.objects.filter(name__icontains =  search)
        categories = Category.objects.all()
        if not products:
            if " " in search:
                print('if1')
                searchsplit = search.split()
                verificador = False
                len_search = len(searchsplit)
                for i in range(len_search):
                    if not verificador:
                        search = search.replace(searchsplit[len_search-(i+1)], "")
                        search2  = search
                        print(search2)
                        products = Product.objects.filter(name__icontains =  search2)
                        if products:
                            verificador = True
                
                if products:
                    categories = products[0].category.department.categories.all()
                else:
                    for i in range(len_search):
                        if not products:
                            products = Product.objects.filter(name__icontains= searchsplit[i])  
                    if products:
                        categories = products[0].category.department.categories.all()       
                    
        else:
            print('else1')
            categories = products[0].category.department.categories.all()
        return render(request, 'search.html', {'products': products, 'categories': categories})
    else:

        return redirect('/home')

class ListCardView(ListView):
    model = Card
    template_name = 'home.html'
    context_object_name = "cards"
class UpdateCardView(HasPermissionsMixin, UpdateView):
    required_permission= 'edit_home_page'
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('ecommerc:home')
class DepartmentView(DetailView):
    model = Department
    template_name = "ecommerc_departments.html"
    context_object_name = "department"
class AdminView(HasPermissionsMixin,TemplateView):
    required_permission= 'edit_all_page'
    template_name = 'admin.html'

    
