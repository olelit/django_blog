from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from user_extend.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegisterForm

    def get_absolute_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



