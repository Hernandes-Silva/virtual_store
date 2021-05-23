
from django.http.response import HttpResponse
from django.shortcuts import render
import mercadopago
from django.urls import reverse
# Create your views here.
def paymentView(request):
    #necessario mudar a url para receber o id do order
    sdk = mercadopago.SDK("TEST-5053757710631102-051117-2db1eede8cb93c0dbe21eb7067c51059-705075200")
    
    preference_data = {
        "items": [

        ],
        "back_urls": {
        "success":  reverse('payment_approved'),
        "failure": reverse('payment_failure'),
        "pending": "http://127.0.0.1:8000/payments/pending"
        },
        "auto_return": "approved"
    }
    #fazer um for no order.items
    preference_data['items'].append({
    "title": "LRoupa intima",
    "description": "Inspired by the classic foldable art of origami",
    "quantity": 3,
    "unit_price": 55.41
    })
    preference_data['items'].append({
    "id": "2",
    "title": "Sexo",
    "description": "IInstrui",
    "quantity": 3,
    "unit_price": 55.41
    })
    print(preference_data['items'])
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return render(request, 'payment.html', {"preference" : preference})
def paymentApprovedView(request):
   return HttpResponse(request.POST)
def paymentFailureView(request):
   return HttpResponse(request.POST)
def paymentPendingView(request):
   return HttpResponse(request.GET['collection_status'])
