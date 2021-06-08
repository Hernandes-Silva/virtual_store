from payment.views import paymentView
from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
    path('payments/proccess/<int:order_id>', views.paymentView, name="payment"),
    path('payments/approved', views.paymentApprovedView, name="payment_approved"),
    path('payments/failure', views.paymentFailureView, name="payment_failure"),
    path('payments/pending', views.paymentPendingView, name="payment_pending"),
    path('payments/list', views.ListPaymentsView.as_view(), name="payment_list"),
    path('payments/user-list/', views.ListUserPaymentsView.as_view(), name="payment_user_list"),
]
    