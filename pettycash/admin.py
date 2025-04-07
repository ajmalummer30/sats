from django.contrib import admin

from pettycash.models import Expense, ExpenseItem

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseItem)
