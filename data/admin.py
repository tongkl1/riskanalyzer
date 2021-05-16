from django.contrib import admin
from .models import BalanceSheet, IncomeSheet, CashflowSheetDirect, CashflowSheetIndirect

admin.site.register(BalanceSheet)
admin.site.register(IncomeSheet)
admin.site.register(CashflowSheetDirect)
admin.site.register(CashflowSheetIndirect)