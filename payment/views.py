
from order.models import Order
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
import mercadopago
from django.urls import reverse
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
         "back_urls": {
         "success":  "http://127.0.0.1:8000/payments/approved",
         "failure": "http://127.0.0.1:8000/payments/failure",
         "pending": "http://127.0.0.1:8000/payments/pending"
         },
         "auto_return": "approved"
      }
      #fazer um for no order.items
      for item in order.items.all():
         preference_data['items'].append({
         "title": item.product.name,
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
   return HttpResponse(request.GET['collection_status'])
def paymentFailureView(request):
   return HttpResponse(request.GET['collection_status'])
def paymentPendingView(request):
   return HttpResponse(request.GET['collection_status'])
