**Backend qismi Django yordamida REST API orqali tuzilgan va JWT autentifikatsiya bilan himoyalangan.**

**Asosiy Texnologiyalar**

**Dasturlash tili**: Python (Django va Django REST Framework)

**Ma’lumotlar bazasi**: PostgreSQL

**Autentifikatsiya**: JWT tokenlar yordamida

**Fayllar saqlash**: Media fayllar (masalan, QR kodlar) uchun Django media sozlamalari


***Yaratilgan API’lar va Ularning Vazifalari***

Backend qismida jami 12 ta API endpoint yaratildi, ular quyidagi modellar uchun CRUD (Create, Read, Update, Delete) operatsiyalarini amalga oshiradi:

# Joytop API

Joytop API — restoranlar va xizmatlarni boshqarish uchun yaratilgan backend tizim. Ushbu API orqali foydalanuvchilar buyurtmalarni boshqarish, stollarni bron qilish, tranzaktsiyalarni kuzatish va boshqa ko‘plab funksiyalardan foydalanishlari mumkin.

---

## 📋 **Asosiy API Endpointlari**

### **1. Payment Methods (`/api/payment-methods/`)**
To‘lov usullarini boshqarish:
- **GET**: Barcha to‘lov usullarining ro‘yxatini qaytaradi.
  - Misol: `["Cash", "Credit Card", "Online Payment"]`
- **POST**: Yangi to‘lov usulini qo‘shadi (admin uchun).
  - Body: 
    ```json
    { "name": "Apple Pay" }
    ```
- **PUT/PATCH**: To‘lov usulini yangilaydi.
  - Body: 
    ```json
    { "name": "Updated Payment Method" }
    ```
- **DELETE**: To‘lov usulini tizimdan o‘chiradi.

---

### **2. Tables (`/api/tables/`)**
Restorandagi stollarni boshqarish:
- **GET**: Barcha stollar ro‘yxatini qaytaradi.
  - Misol: 
    ```json
    [{ "id": 1, "number": "A1", "capacity": 4 }]
    ```
- **POST**: Yangi stolni qo‘shadi.
  - Body:
    ```json
    { "number": "B2", "capacity": 6 }
    ```
- **PUT/PATCH**: Stol ma’lumotlarini yangilaydi.
  - Body:
    ```json
    { "capacity": 5 }
    ```
- **DELETE**: Stolni o‘chiradi.

---

### **3. User Roles (`/api/user-roles/`)**
Foydalanuvchi rollarini boshqarish:
- **GET**: Rollar ro‘yxatini qaytaradi.
  - Misol: `["Admin", "Waiter", "Customer"]`
- **POST**: Yangi rol qo‘shadi.
  - Body:
    ```json
    { "role": "Manager" }
    ```
- **PUT/PATCH**: Rolni yangilaydi.
  - Body:
    ```json
    { "role": "Updated Role" }
    ```
- **DELETE**: Rolni tizimdan o‘chiradi.

---

### **4. Users (`/api/users/`)**
Foydalanuvchilarni boshqarish:
- **GET**: Barcha foydalanuvchilar ro‘yxatini qaytaradi.
  - Misol: 
    ```json
    [{ "id": 1, "username": "JohnDoe", "role": "Customer" }]
    ```
- **POST**: Yangi foydalanuvchini tizimga qo‘shadi.
  - Body:
    ```json
    { "username": "JaneDoe", "password": "securepassword", "role": "Waiter" }
    ```
- **PUT/PATCH**: Foydalanuvchi ma’lumotlarini yangilaydi.
  - Body:
    ```json
    { "password": "newsecurepassword" }
    ```
- **DELETE**: Foydalanuvchini tizimdan o‘chiradi.

---

### **5. Orders (`/api/orders/`)**
Buyurtmalarni boshqarish:
- **GET**: Barcha buyurtmalar ro‘yxatini qaytaradi.
  - Misol:
    ```json
    [{ "id": 1, "table": "A1", "items": ["Pizza", "Cola"], "status": "Pending" }]
    ```
- **POST**: Yangi buyurtma yaratadi.
  - Body:
    ```json
    { "table_id": 1, "items": [1, 2] }
    ```
- **PUT/PATCH**: Buyurtmani yangilaydi.
  - Body:
    ```json
    { "status": "Completed" }
    ```
- **DELETE**: Buyurtmani tizimdan o‘chiradi.

---

### **6. Menu Items (`/api/menu-items/`)**
Menyu elementlarini boshqarish:
- **GET**: Menyudagi barcha taomlarni qaytaradi.
  - Misol:
    ```json
    [{ "id": 1, "name": "Pizza", "price": 12.99 }]
    ```
- **POST**: Yangi menyu elementi qo‘shadi.
  - Body:
    ```json
    { "name": "Burger", "price": 9.99 }
    ```
- **PUT/PATCH**: Menyu elementini yangilaydi.
  - Body:
    ```json
    { "price": 10.99 }
    ```
- **DELETE**: Menyu elementini o‘chiradi.

---

### **7. Checks (`/api/checks/`)**
Hisob-kitoblarni boshqarish:
- **GET**: Hisob-kitoblar ro‘yxatini qaytaradi.
  - Misol:
    ```json
    [{ "id": 1, "order_id": 1, "total": 25.98 }]
    ```
- **POST**: Yangi hisob-kitob qo‘shadi.
  - Body:
    ```json
    { "order_id": 1, "total": 25.98 }
    ```
- **PUT/PATCH**: Hisob-kitobni yangilaydi.
  - Body:
    ```json
    { "total": 30.00 }
    ```
- **DELETE**: Hisobni tizimdan o‘chiradi.

---

### **8. Transactions (`/api/transactions/`)**
Tranzaktsiyalarni boshqarish:
- **GET**: Tranzaktsiyalar ro‘yxatini qaytaradi.
  - Misol:
    ```json
    [{ "id": 1, "payment_method": "Credit Card", "amount": 25.98 }]
    ```
- **POST**: Yangi tranzaktsiya qo‘shadi.
  - Body:
    ```json
    { "order_id": 1, "payment_method": "Credit Card", "amount": 25.98 }
    ```
- **DELETE**: Tranzaktsiyani tizimdan o‘chiradi.

---

### **9. Reports (`/api/reports/`)**
Hisobotlarni boshqarish:
- **GET**: Hisobotlar ro‘yxatini qaytaradi.
- **POST**: Yangi hisobot yaratadi.
  - Body:
    ```json
    { "type": "daily", "data": { "revenue": 1500 } }
    ```
- **DELETE**: Hisobotni tizimdan o‘chiradi.

---

### **10. Discounts (`/api/discounts/`)**
Chegirmalarni boshqarish:
- **GET**: Chegirmalar ro‘yxatini qaytaradi.
  - Misol:
    ```json
    [{ "id": 1, "name": "10% Off", "amount": 10 }]
    ```
- **POST**: Yangi chegirma qo‘shadi.
  - Body:
    ```json
    { "name": "Holiday Special", "amount": 15 }
    ```
- **PUT/PATCH**: Chegirma ma’lumotlarini yangilaydi.
  - Body:
    ```json
    { "amount": 20 }
    ```
- **DELETE**: Chegirmani tizimdan o‘chiradi.

---

### **11. Reservations (`/api/reservations/`)**
Stollarni bron qilish:
- **GET**: Bron qilingan stollar ro‘yxatini qaytaradi.
- **POST**: Stol bronlash.
  - Body:
    ```json
    { "table_id": 1, "customer_name": "John Doe", "time": "2024-11-15T19:00:00" }
    ```
- **PUT/PATCH**: Bronni yangilaydi.
- **DELETE**: Bronni tizimdan o‘chiradi.

---

### **12. Feedbacks (`/api/feedbacks/`)**
Foydalanuvchilar fikr-mulohazalarini boshqarish:
- **GET**: Fikr-mulohazalar ro‘yxatini qaytaradi.
- **POST**: Yangi fikr-mulohaza qo‘shadi.
  - Body:
    ```json
    { "customer_name": "John Doe", "message": "Great service!" }
    ```
- **DELETE**: Fikrni tizimdan o‘chiradi.

---

## 🔧 **Texnologiyalar**
- **Backend**: Django Rest Framework
- **Ma’lumotlar Bazasi**: PostgreSQL
- **Caching**: Redis
- **Autentifikatsiya**: JWT

---

Agar yana qo‘shimcha savollar bo‘lsa, [Issues](https://github.com/yourusername/joytop-api/issues) bo‘limiga murojaat qiling. 😊


**Umumiy Xulosa**

Joytop loyihasining backend qismi Django yordamida ishlab chiqilgan bo‘lib, 12 ta asosiy API endpointlari orqali foydalanuvchilar, buyurtmalar, menyu, rezervatsiyalar va boshqa asosiy funksiyalarni boshqarish imkonini beradi. Loyihaning backend qismi REST API’lar bilan to‘liq ta’minlangan va JWT autentifikatsiya bilan himoyalangan. Bu holatda ilova foydalanuvchilar uchun xavfsiz va oson boshqariladigan bo‘lib qoladi.
