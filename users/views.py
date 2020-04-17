from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms
from . import models

# Create your views here.

class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
