from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404


def transaction_list(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    # Fixed the parenthesis/bracket placement here:
    total_income = Transaction.objects.filter(transaction_type='INCOME').aggregate(total=Sum('amount'))['total'] or 0
    total_expense = Transaction.objects.filter(transaction_type='EXPENSE').aggregate(total=Sum('amount'))['total'] or 0
    total_balance = total_income - total_expense
        
    transactions = Transaction.objects.all() # (minor naming tip: plural 'transactions' is cleaner for a list)
    
    # Added 'total_balance' to the context dictionary:
    context = {
        'transactions': transactions, 
        'form': form,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance,
    }
    return render(request, 'index.html', context)


def delete_transaction(request, pk):
    get_object_or_404(Transaction, pk=pk).delete()
    return redirect('transaction_list')
