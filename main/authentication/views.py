from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegistrationView(generic.CreateView):
    form_class = UserCreationForm # This provides Username/ Password fields for later
    template_name = "registration/Register.html"
    success_url = reverse_lazy('login')
    # The first thing you`re going to want after success registration is login.

