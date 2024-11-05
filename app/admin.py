# restaurant_payment/admin.py
from django.contrib import admin
from .models import PaymentMethod, Table, UserRole, User, Check, Transaction, Report

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'method_name', 'description')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'qr_code_data', 'qr_code_image')  # `qr_code_image_url` o'rniga `qr_code_image`

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_qr_code', 'user_payment', 'user_role', 'created_at')

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'check_sum', 'tax_amount', 'final_total', 
                    'payment_method', 'paid_status', 'created_at', 'updated_at')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_reference', 'payment_method', 'amount', 'transaction_date', 'status')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_reference', 'user', 'payment_method', 'report_date', 
                    'total_sales', 'report_type', 'total_transactions', 'created_at')
