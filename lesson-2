1.
ism = input("Iltimos, ismingizni kiriting:")
tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
joriy_yil = (2025)
print ( ism, joriy_yil - tugilgan_yil)
Axadjon 35
2.
txt = 'LMaasleitbtui'
txt[1::2]
'Malibu'
3.
txt = 'MsaatmiazD'
txt[::2]
'Matiz'
4.
txt = "I'am John. I am from London"
txt[-6:]
'London'
5.
txt = "London"
txt[::-1]
'nodnoL'
6.
matn = input("Matn kiriting: ")
unlilar = ['a', 'e', 'i', 'o', 'u', 'o‘']
soni = 0
for harf in matn:
if harf in unlilar:
soni += 1
print(f"Matndagi unlilar soni: {soni}")
Matndagi unlilar soni: 7
assalomu alaykum
7.
raqamlar_str = input("Raqamlarni bo'sh joy bilan kiriting: ")
raqamlar = list(map(int, raqamlar_str.split()))
maks_raqam = max(2,6,8,9,15,25,79)
print(f"Eng katta raqam: {maks_raqam}")
Eng katta raqam: 79
8.
soz = input("So'z kiriting: ")
if soz == soz[::-1]:
print("Bu so'z palindrom.")
else:
print("Bu so'z palindrom emas.")
Bu so'z palindrom. kiyik
9.
email = input("Elektron pochta manzilingizni kiriting: ")
try:
domen = email.split('@')[1]
print(f"Domen: {domen}")
except IndexError:
print("Noto'g'ri elektron pochta manzili kiritildi.")
Domen: gmail.com
10.
import random
import string
def parol_yarat(uzunlik=12):
# Belgilar to'plami
harflar = string.ascii_letters # Katta va kichik harflar
raqamlar = string.digits # Raqamlar 0-9
maxsus_belgilar = string.punctuation # Maxsus belgilar
# Har bir turdan kamida bittadan olish uchun
parol =
    random.choice(harflar),
    random.choice(raqamlar),
    random.choice(maxsus_belgilar)
# Qolgan belgilarni tasodifiy to'ldirish
qolgan = uzunlik - len(parol)
hammasi = harflar + raqamlar + maxsus_belgilar
parol += random.choices(hammasi, k=qolgan)
# Belgilar tartibini aralashtirish
random.shuffle(parol)
return ''.join(parol)
11.
tasodifiy_parol = parol_yarat(12) # uzunligi 12 belgidan iborat
print("Yaratilgan parol:", tasodifiy_parol)
Yaratilgan parol: 1<A]4](,\D1U
