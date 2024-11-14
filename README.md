**Backend qismi Django yordamida REST API orqali tuzilgan va JWT autentifikatsiya bilan himoyalangan.**

**Asosiy Texnologiyalar**

**Dasturlash tili**: Python (Django va Django REST Framework)

**Ma’lumotlar bazasi**: PostgreSQL

**Autentifikatsiya**: JWT tokenlar yordamida

**Fayllar saqlash**: Media fayllar (masalan, QR kodlar) uchun Django media sozlamalari


***Yaratilgan API’lar va Ularning Vazifalari***

Backend qismida jami 12 ta API endpoint yaratildi, ular quyidagi modellar uchun CRUD (Create, Read, Update, Delete) operatsiyalarini amalga oshiradi:

**PaymentMethod API**

Vazifasi: To‘lov usullarini boshqarish, to‘lov usullari haqida ma’lumot qo‘shish, yangilash va o‘chirish.

**Table API**

Vazifasi: Restoran stol ma'lumotlarini boshqarish, QR kod yaratish va saqlash. Bu API orqali har bir stol uchun QR kod generatsiya qilinadi va saqlanadi.

**UserRole API**

Vazifasi: Foydalanuvchi rollarini boshqarish, har bir foydalanuvchining rolini belgilash.

**User API**

Vazifasi: Foydalanuvchilarni boshqarish, foydalanuvchilarni qo‘shish, yangilash va o‘chirish. Foydalanuvchilar uchun rollarni va to‘lov statuslarini belgilaydi.

**Order API**

Vazifasi: Buyurtmalarni boshqarish, har bir buyurtma uchun QR kod yaratish. Bu API orqali foydalanuvchilar buyurtmalarini yaratish, yangilash va boshqarish imkoniyatiga ega bo‘ladi.

**MenuItem API**

Vazifasi: Restoran menyu elementlarini boshqarish, menyu qo‘shish, o‘chirish, va yangilash. Ushbu API orqali foydalanuvchilar menyudan buyurtma qilishlari mumkin.

**Check API**

Vazifasi: Cheklar yaratish va boshqarish. Bu API orqali hisoblarni qo'shish, yangilash va ularning to'lov holatini kuzatish mumkin.

**Transaction API**

Vazifasi: To‘lov tranzaksiyalarini boshqarish. Bu API orqali to‘lovlarning miqdori, holati va ularni amalga oshirish vaqti kuzatiladi.

**Report API**

Vazifasi: Hisobotlar yaratish va boshqarish, foydalanuvchi va to'lov usuli asosida hisobot olish. Bu API orqali kunlik, haftalik yoki oylik savdo hisobotlarini yaratish mumkin.

**Discount API**

Vazifasi: Chegirmalarni boshqarish, chegirmalar haqida ma’lumot qo‘shish, yangilash va boshqarish.

**Reservation API**

Vazifasi: Stol rezervatsiyalarini boshqarish, foydalanuvchilarga oldindan stol band qilish imkonini beradi.

**Feedback API**

Vazifasi: Fikr-mulohazalarni boshqarish, foydalanuvchilarga restoran va xizmatlar haqida fikr bildirish imkonini beradi.

**Autentifikatsiya va Xavfsizlik**

Barcha API’lar JWT tokenlar orqali autentifikatsiya qilinadi. Foydalanuvchilar api/token/ endpoint orqali tizimga kirish uchun token olishadi va har bir so'rovda ushbu tokenni yuborishlari talab qilinadi.

**Umumiy Xulosa**

Joytop loyihasining backend qismi Django yordamida ishlab chiqilgan bo‘lib, 12 ta asosiy API endpointlari orqali foydalanuvchilar, buyurtmalar, menyu, rezervatsiyalar va boshqa asosiy funksiyalarni boshqarish imkonini beradi. Loyihaning backend qismi REST API’lar bilan to‘liq ta’minlangan va JWT autentifikatsiya bilan himoyalangan. Bu holatda ilova foydalanuvchilar uchun xavfsiz va oson boshqariladigan bo‘lib qoladi.
