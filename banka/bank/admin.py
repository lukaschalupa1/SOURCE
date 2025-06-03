from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Customer, Account, Loan, CreditCard, Investment

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(CreditCard)
admin.site.register(Investment)