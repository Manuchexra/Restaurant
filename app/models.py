# restaurant/models.py
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True)
    items = models.TextField()  # Mahsulotlar ro'yxati (JSON yoki boshqa formatda)
    total_amount = models.FloatField()
    order_status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('completed', 'Completed')], 
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code_image = models.ImageField(upload_to='order_qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - Status: {self.order_status}"

    def save(self, *args, **kwargs):
        # Buyurtma haqida QR kod yaratish
        qr_data = f"Order ID: {self.id}\nTotal Amount: {self.total_amount}"
        qr = qrcode.make(qr_data)
        qr_image = BytesIO()
        qr.save(qr_image, format='PNG')
        qr_image.seek(0)
        self.qr_code_image.save(f"order_{self.id}_qr.png", File(qr_image), save=False)
        super().save(*args, **kwargs)

import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.utils import timezone

# To'lov usullari modeli
class PaymentMethod(models.Model):
    method_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.method_name

# Stol modeli va QR kod yaratish funksiyasi
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    qr_code_data = models.URLField()
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Table {self.table_number}"

    def save(self, *args, **kwargs):
        # QR kod yaratish
        qr = qrcode.make(self.qr_code_data)
        qr_image = BytesIO()
        qr.save(qr_image, format='PNG')
        qr_image.seek(0)
        self.qr_code_image.save(f"table_{self.table_number}_qr.png", File(qr_image), save=False)
        super().save(*args, **kwargs)

# Foydalanuvchi roli modeli
class UserRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

# Foydalanuvchi modeli
class User(models.Model):
    user_qr_code = models.ImageField(upload_to='qr_codes/')
    user_payment = models.BooleanField(default=False)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.id} - Role: {self.user_role}"

# Menyu elementi modeli
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Chek modeli
class Check(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    check_sum = models.FloatField()
    tax_amount = models.FloatField()
    final_total = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    paid_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Check {self.id} - Total: {self.final_total}"

# Tranzaksiya modeli
class Transaction(models.Model):
    check_reference = models.ForeignKey(Check, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"Transaction {self.id} - Amount: {self.amount}"

# Hisobot modeli
class Report(models.Model):
    check_reference = models.ForeignKey(Check, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    report_date = models.DateTimeField()
    total_sales = models.FloatField()
    report_type = models.CharField(max_length=50)
    total_transactions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - Type: {self.report_type}"

# Chegirma modeli
class Discount(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    discount_percent = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.discount_percent}%"

# Rezervatsiya modeli
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    guests = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('reserved', 'Reserved'), ('cancelled', 'Cancelled')], default='reserved')

    def __str__(self):
        return f"Reservation for {self.user} on {self.reservation_date}"

# Fikr-mulohaza modeli
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user} - Rating: {self.rating}"

