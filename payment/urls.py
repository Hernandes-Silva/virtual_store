from payment.views import paymentView
from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
    path('test/', views.paymentView, name="payment"),
    path('payments/approved', views.paymentApprovedView, name="payment_approved"),
    path('payments/failure', views.paymentFailureView, name="payment_failure"),
    path('payments/pending', views.paymentPendingView, name="payment_pending"),
]
    