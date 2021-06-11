from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.detail import DetailView
from products.models import Department, Category, Product, TechnicalInformation
from django.forms.models import inlineformset_factory
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from products.forms import *
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.mixins import HasPermissionsMixin



# Create your views here.
@has_permission_decorator('edit_all_page', redirect_to_login = reverse_lazy('login'))
def CreateProduct(request):
    product_forms = Product()
    
    technical_information_formset = inlineformset_factory(Product, TechnicalInformation, form=TechnicalInformationForm, extra=0, can_delete=False, min_num=1, validate_min=True)
    if request.method == 'POST':
        
        forms = ProductForm(request.POST, request.FILES, prefix='main')
        if forms.is_valid():
            
            product = forms.save()
            formset = technical_information_formset(request.POST, request.FILES, instance=product, prefix='product')
            
            if  formset.is_valid():
                
                formset.save()
                return HttpResponseRedirect(reverse_lazy('product_detail', args=[product.pk]))
    else:
        forms = ProductForm(instance=product_forms, prefix='main')
        formset = technical_information_formset(prefix='product')
        
    context = {
        'form': forms,
        'formset': formset,
    }

    return render(request, 'product_create.html', context)
class ListDepartmentView(HasPermissionsMixin, ListView):
    required_permission = 'edit_all_page'
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'
class CreateDepartmentView(HasPermissionsMixin, CreateView):
    model = Department
    required_permission = 'edit_all_page'
    form_class = DepartmentForm
    template_name= "department_create.html"
    success_url = reverse_lazy('department_list')
class UpdateDepartmentView(HasPermissionsMixin, UpdateView):
    required_permission = 'edit_all_page'
    model = Department
    form_class = DepartmentForm
    template_name = 'department_update.html'
    success_url = reverse_lazy('department_list')
class ListCategoryView(HasPermissionsMixin, ListView):
    model = Category
    required_permission = 'edit_all_page'
    template_name = "category_list.html"
    context_object_name = 'categories'
class CreateCategoryView(HasPermissionsMixin, CreateView):
    model = Category
    required_permission = 'edit_all_page'
    form_class = CategoryForm
    template_name = "category_create.html"
    success_url = reverse_lazy('category_list')
class UpdateCategoryView(HasPermissionsMixin, UpdateView):
    required_permission = 'edit_all_page'
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')
class DetailProductView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = "product"
class ListProductView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = 'products'
class UpdateProductView(HasPermissionsMixin, UpdateView):
    model = Product
    required_permission = 'edit_all_page'
    form_class = ProductForm
    template_name = "product_update.html"
    def get_context_data(self, **kwargs):
        context = super(UpdateProductView, self).get_context_data(**kwargs)
        technical_information_formset = inlineformset_factory(Product, TechnicalInformation, form=TechnicalInformationForm, extra=0, can_delete=False, min_num=1, validate_min=True)
        if self.request.POST:
            context['formset'] = technical_information_formset(self.request.POST, instance=self.object, prefix='product')
        else:
            context['formset'] = technical_information_formset(instance=self.object, prefix='product')
        return context
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(reverse_lazy('product_detail', args=[self.object.pk]))

