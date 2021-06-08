
from django.urls import path
from e_commerc import views
app_name = 'ecommerc'
urlpatterns = [
    path('', views.ListCardView.as_view()),
    path('home/', views.ListCardView.as_view(), name="home"),
    path('card/<int:pk>/update/', views.UpdateCardView.as_view(), name="card_update"),
    path('departamentos/<slug:slug>/', views.DepartmentView.as_view(), name="department"),
    path('departamentos/<slug:department_slug>/<slug:slug>', views.CategoryView, name="category"),
    path('departamentos/<slug:department_slug>/<slug:slug>', views.CategoryView, name="category"),
    path('administrador/', views.AdminView.as_view(), name="administrador"),
    path('busca/', views.searchView, name="search"),
]