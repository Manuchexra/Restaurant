# restaurant/admin.py
from django.contrib import admin
from .models import (
    PaymentMethod, Table, UserRole, User, Order, MenuItem, Check,
    Transaction, Report, Discount, Reservation, Feedback
)

admin.site.register(PaymentMethod)
admin.site.register(Table)
admin.site.register(UserRole)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Check)
admin.site.register(Transaction)
admin.site.register(Report)
admin.site.register(Discount)
admin.site.register(Reservation)
admin.site.register(Feedback)
