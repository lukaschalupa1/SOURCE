from . formular import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
    else:
        form = RegistrationForm()
    
    return render(request, "banka\sign_up.html", {
        "form":form
        })

from django.shortcuts import render
from .models import Customer, Account, Loan, CreditCard, Investment, Forextransaction, Automaticpayment

def index(request):
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    loans = Loan.objects.all()
    credit_cards = CreditCard.objects.all()
    investments = Investment.objects.all()

    context = {
        "customers": customers,
        "accounts": accounts,
        "loans": loans,
        "credit_cards": credit_cards,
        "investments": investments,
    }
    return render(request, "banka/index.html", context)