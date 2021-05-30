
from django.urls import path
from e_commerc import views
app_name = 'ecommerc'
urlpatterns = [
    path('<slug:slug>/', views.DepartmentView.as_view(), name="department"),
    path('<slug:department_slug>/<slug:slug>', views.CategoryView, name="category"),

]