from django.db import models

TRANSCATION_TYPES = (
    ('INCOME', 'Income'),
    ('EXPENSE','Expense'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Savings(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = "Savings"

    def __str__(self):
        return f"{self.name} ({self.current_amount}/{self.target_amount})"


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Optional link to a savings goal if this transaction is a savings contribution
    savings_goal = models.ForeignKey(Savings, on_delete=models.SET_NULL, null=True, blank=True)
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10, 
        choices=[('INCOME', 'Income'), ('EXPENSE', 'Expense'), ('SAVINGS', 'Savings')]
    )
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSCATION_TYPES,
        default='INCOME'
    )


    def __str__(self):
        return f"{self.description}"