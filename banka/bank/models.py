from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    contact_info = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"    

class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=32, unique=True)
    account_type = models.CharField(max_length=32)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)
    created_at = models.DateField()
    
    def __str__(self):
        return f"{self.account_number} ({self.account_type})"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="loans")
    loan_type = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    monthly_payment = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.loan_type} - {self.amount} CZK"

class CreditCard(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="credit_cards")
    card_type = models.CharField(max_length=32)
    limit = models.DecimalField(max_digits=15, decimal_places=2)
    annual_fee = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField()
    
    def __str__(self):
        return f"{self.card_type} ({'Active' if self.active else 'Inactive'})"

class Investment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="investments")
    investment_type = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    annual_return = models.DecimalField(max_digits=5, decimal_places=2)
    risk_level = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.investment_type} - {self.amount} CZK"

class Forextransaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="forex_transactions")
    original_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=5)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.amount} {self.original_currency} to {self.target_currency}"

class Automaticpayment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="automatic_payments")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    frequency = models.CharField(max_length=32)
    first_payment_date = models.DateField()
    last_payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.amount} CZK ({self.frequency})"