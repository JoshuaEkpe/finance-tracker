from .models import Transaction
from django import forms 


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'category', 'transaction_type',]