from django.urls import path
from accounts import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name="user_create"),
]