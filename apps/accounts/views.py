from django.shortcuts import render
from allauth.account.views import LoginView


class MyLogin(LoginView):
    template_name = "account/login.html"
