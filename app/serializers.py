# restaurant_payment/serializers.py
from rest_framework import serializers
from .models import PaymentMethod, Table, UserRole, User, Check, Transaction, Report

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'method_name', 'description']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'table_number', 'qr_code_data', 'qr_code_image_url', 'qr_code_image']

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id', 'role_name']

class UserSerializer(serializers.ModelSerializer):
    user_role = UserRoleSerializer()

    class Meta:
        model = User
        fields = ['id', 'user_qr_code', 'user_payment', 'user_role', 'created_at']

class CheckSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    table = TableSerializer()
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Check
        fields = ['id', 'user', 'table', 'check_sum', 'tax_amount', 'final_total', 
                  'payment_method', 'paid_status', 'created_at', 'updated_at']

class TransactionSerializer(serializers.ModelSerializer):
    check_reference = CheckSerializer()  # `check` maydoni `check_reference` deb o'zgartirildi
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'check_reference', 'payment_method', 'amount', 'transaction_date', 'status']

class ReportSerializer(serializers.ModelSerializer):
    check_reference = CheckSerializer()  # `check` maydoni `check_reference` deb o'zgartirildi
    user = UserSerializer()
    payment_method = PaymentMethodSerializer()

    class Meta:
        model = Report
        fields = ['id', 'check_reference', 'user', 'payment_method', 'report_date', 
                  'total_sales', 'report_type', 'total_transactions', 'created_at']
