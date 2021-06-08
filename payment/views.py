
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Order
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
import mercadopago
from django.contrib.auth.decorators import login_required
from payment.models import Payment
from django.urls import reverse
import requests
from rolepermissions.mixins import HasRoleMixin
from django.views.generic import ListView, CreateView
# Create your views here.

@login_required
def paymentView(request, order_id):
    sdk = mercadopago.SDK(
        "TEST-5053757710631102-051117-2db1eede8cb93c0dbe21eb7067c51059-705075200")
    order = get_object_or_404(Order, id=order_id)
    if not order.paid:
        preference_data = {
            "items": [

            ],
            "auto_return": "approved",
            "back_urls": {
                "success":  "http://127.0.0.1:8000/payments/approved",
                "failure": "http://127.0.0.1:8000/payments/failure",
                "pending": "http://127.0.0.1:8000/payments/pending"
            }

        }
        for item in order.items.all():
            preference_data['items'].append({
                "title": str(order_id),
                "description": item.product.information,
                "quantity": item.quantity,
                "unit_price": float(item.price)
            })
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        return render(request, 'payment.html', {"preference": preference, "items":order.items.all(), 'total_price':order.get_total_price})
    return redirect(reverse('home'))

@login_required
def paymentApprovedView(request):
   if request.GET['payment_id']:
      payment_id = request.GET['payment_id']
      url = create_payment(payment_id,request)
      if url:
         return url
   return redirect(reverse('ecommerc:home'))

@login_required
def paymentFailureView(request):
   if request.GET['payment_id']:
      payment_id = request.GET['payment_id']
      url = create_payment(payment_id,request)
      if url:
         return url
   return redirect(reverse('ecommerc:home'))

@login_required
def paymentPendingView(request):
   if request.GET['payment_id']:
      payment_id = request.GET['payment_id']
      url = create_payment(payment_id,request)
      if url:
         return url
   return redirect(reverse('ecommerc:home'))


def create_payment(payment_id, request):
   payment_test = Payment.objects.filter(mercadopago_id=payment_id)
   if not payment_test:
      url = "https://api.mercadopago.com//v1/payments/"+payment_id + \
            "?access_token=TEST-5053757710631102-051117-2db1eede8cb93c0dbe21eb7067c51059-705075200"
      payment = requests.get(url)
      payment = payment.json()
      order = Order.objects.get(id=int(payment['description']))
      object_pay = Payment.objects.create(user = request.user, order = order,mercadopago_id = payment['id'],
         status = payment['status'], status_detail = payment['status_detail'], installments = payment['installments'],
         payment_method= payment['payment_method_id'], payment_type = payment['payment_type_id'])
      if payment['status'] == "approved":
         order.paid = True
         order.save()
         return render(request, "success.html", {"payment": object_pay})
      elif payment['status'] == "in_process":
         return render(request, "pending.html", {"payment": object_pay})
      else:
         return render(request, "failure.html", {"payment": object_pay})
   return False
class ListUserPaymentsView(LoginRequiredMixin, ListView):
   model = Payment
   template_name = 'payment_user_list.html'
   context_object_name = "payments"
   def get_queryset(self):
        payments = Payment.objects.filter(user = self.request.user)
        return payments
class ListPaymentsView(HasRoleMixin, ListView):
   allowed_roles = 'MasterMember'
   model = Payment
   template_name = 'list_payments.html'
   context_object_name = "payments"
   
   



