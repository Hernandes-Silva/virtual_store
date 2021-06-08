from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('department/', views.ListDepartmentView.as_view(), name="department_list"),
    path('department/create', views.CreateDepartmentView.as_view(), name="department_create"),
    path('department/<int:pk>/update', views.UpdateDepartmentView.as_view(), name="department_update"),
    path('category/', views.ListCategoryView.as_view(), name="category_list"),
    path('category/create', views.CreateCategoryView.as_view(), name = "category_create"),
    path('category/<int:pk>/update', views.UpdateCategoryView.as_view(), name="category_update"),
    path('products/', views.ListProductView.as_view(), name="products"),
    path('products/<int:pk>/', views.DetailProductView.as_view(), name="product_detail"),
    path('products/<int:pk>/update/', views.UpdateProductView.as_view(), name="product_update"),
    path('products/create/', views.CreateProduct, name = "product_create"),
]