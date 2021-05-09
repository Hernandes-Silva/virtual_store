from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('department/', views.ListDepartmentView.as_view(), name="department_list"),
    path('department/create', views.CreateDepartmentView.as_view(), name="department_create"),
    path('category/', views.ListCategoryView.as_view(), name="category_list"),
    path('category/create', views.CreateCategoryView.as_view(), name = "category_create"),
    path('home/', views.ListProductView.as_view(), name="home"),
    path('products/create', views.CreateProductView.as_view(), name = "product_create"),
]