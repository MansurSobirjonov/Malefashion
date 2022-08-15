from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import *


# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)
