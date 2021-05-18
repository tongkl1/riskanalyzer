from django.contrib import admin
from .models import *

admin.site.register(BasicInformation)
admin.site.register(BalanceSheet)
admin.site.register(IncomeSheet)
admin.site.register(CashflowSheetDirect)
admin.site.register(CashflowSheetIndirect)
admin.site.register(ReportAudit)