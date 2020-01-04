from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return render(response, 'register/success_register.html')
        else:
            return render(response, 'register/failed_register.html')
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})




