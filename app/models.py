import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

class PaymentMethod(models.Model):
    method_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.method_name

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

class UserRole(models.Model):
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name

class User(models.Model):
    user_qr_code = models.ImageField(upload_to='qr_codes/')
    user_payment = models.BooleanField(default=False)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.id} - Role: {self.user_role}"

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

class Transaction(models.Model):
    check_reference = models.ForeignKey(Check, on_delete=models.CASCADE)  # 'check' o'rniga 'check_reference' deb nomlandi
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"Transaction {self.id} - Amount: {self.amount}"

class Report(models.Model):
    check_reference = models.ForeignKey(Check, on_delete=models.CASCADE)  # 'check' o'rniga 'check_reference' deb nomlandi
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    report_date = models.DateTimeField()
    total_sales = models.FloatField()
    report_type = models.CharField(max_length=50)
    total_transactions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - Type: {self.report_type}"
