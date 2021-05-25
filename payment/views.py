
from order.models import Order
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
import mercadopago
from payment.models import Payment
from django.urls import reverse
import requests
# Create your views here.
def paymentView(request, order_id):
    #necessario mudar a url para receber o id do order
   print("aquiii2")
   sdk = mercadopago.SDK("TEST-5053757710631102-051117-2db1eede8cb93c0dbe21eb7067c51059-705075200")
   order = get_object_or_404(Order, id = order_id)
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
      #fazer um for no order.items
      for item in order.items.all():
         preference_data['items'].append({
         "title": str(order_id),
         "description": item.product.information,
         "quantity": item.quantity,
         "unit_price": float(item.price)
         })
      print(preference_data['items'])
      preference_response = sdk.preference().create(preference_data)
      preference = preference_response["response"]
      return render(request, 'payment.html', {"preference" : preference})
   return redirect(reverse('home'))

def paymentApprovedView(request):
   if request.GET['payment_id']:
      payment_id = request.GET['payment_id']
      payment_test = Payment.objects.get(mercadopago_id=payment_id)
      if not payment_test:
         payment_id = request.GET['payment_id']
         url = "https://api.mercadopago.com//v1/payments/"+payment_id+"?access_token=TEST-5053757710631102-051117-2db1eede8cb93c0dbe21eb7067c51059-705075200"
         payment = requests.get(url)
         payment = payment.json()
         order = Order.objects.get(id=int(payment['description']))
         order.paid = True
         order.save()
         object_pay = Payment.objects.create(order = order,mercadopago_id = payment_id,
         status = payment['status'], status_detail = payment['status_detail'], installments = payment['installments'],
         payment_method= payment['payment_method_id'], payment_type = payment['payment_type_id'])
         return render(request, "my_payment.html", {"payment":object_pay})
   return redirect(reverse('home'))
def paymentFailureView(request):
   return HttpResponse(request.GET['collection_status'])
def paymentPendingView(request):
   return HttpResponse(request.GET['collection_status'])
""" 
collection_id=1237083248&collection_status=approved&
payment_id=1237083248
&status=approved
&external_reference=null
&payment_type=credit_card&merchant_order_id=2719304120
&preference_id=705075200-aed5c712-9828-42b8-90ad-5a3644f845b3
&site_id=MLB
&processing_mode=aggregator
&merchant_account_id=null """