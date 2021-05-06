from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('department/', views.ListDepartmentView.as_view(), name="department_list"),
    path('department/create', views.CreateDepartmentView.as_view(), name="department_create"),
]