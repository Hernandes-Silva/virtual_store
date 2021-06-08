from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rolepermissions.roles import assign_role
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        assign_role(user, 'client')
        return HttpResponseRedirect(reverse_lazy('login'))
