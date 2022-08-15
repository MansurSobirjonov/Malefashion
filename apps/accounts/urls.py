from django.urls import path
from allauth.account.views import LoginView, SignupView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', LoginView.as_view(template_name='account/login.html'), name='account_signup'),
]
