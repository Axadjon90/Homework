1)try:
    a = int(input("Bo‘linuvchi sonni kiriting: "))
    b = int(input("Bo‘luvchini kiriting: "))
    print("Natija:", a / b)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas.")
  5.5
Natija: 1.0

try:
    number = int(input("Butun son kiriting: "))
except ValueError:
    print("Xatolik: Butun son kiritilmadi.")

try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
  Xatolik: Fayl topilmadi.

try:
    x = input("Birinchi raqamni kiriting: ")
    y = input("Ikkinchi raqamni kiriting: ")
    if not (x.isdigit() and y.isdigit()):
        raise TypeError("Faqat sonli qiymatlar kerak.")
    print("Yig‘indi:", int(x) + int(y))
except TypeError as e:
    print("Xatolik:", e)
  6.9
Yig‘indi: 15

try:
    with open("/root/secret.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Xatolik: Faylga ruxsat yo‘q.")

try:
    my_list = [10, 20, 30]
    index = int(input("Indeksni kiriting (0-2): "))
    print("Qiymat:", my_list[index])
except IndexError:
    print("Xatolik: Indeks ro‘yxat chegarasidan tashqarida.")
  Xatolik: Indeks ro‘yxat chegarasidan tashqarida.

    try:
    number = int(input("Iltimos, raqam kiriting: "))
    print("Kiritilgan raqam:", number)
except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi (Ctrl+C bosildi).")
Kiritilgan raqam: 6

try:
    x = 10
    y = int(input("Bo‘luvchini kiriting: "))
    result = x / y
    print("Natija:", result)
except ArithmeticError:
    print("Xatolik: Arifmetik xatolik yuz berdi.")
  6
Natija: 1.6666666666666667

try:
    with open("somefile.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Xatolik: Faylni kodlashda muammo (UnicodeDecodeError).")

try:
    my_list = [1, 2, 3]
    my_list.upper()
except AttributeError:
    print("Xatolik: Ob'ektda bu atribut (yoki metod) mavjud emas.")
Xatolik: Ob'ektda bu atribut (yoki metod) mavjud emas.

2)with open("fayl.txt", "r") as file:
    print(file.read())
  
  n = 3
with open("fayl.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")

with open("fayl.txt", "a") as file:
    file.write("\nBu yangi qo‘shilgan matn.")
with open("fayl.txt", "r") as file:
    print(file.read())
  Bu yangi qo‘shilgan matn.

    n = 3
with open("fayl.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end="")
      Bu yangi qo‘shilgan matn.

with open("fayl.txt", "r") as file:
    satrlar = file.readlines()
print(satrlar)
['\n', 'Bu yangi qo‘shilgan matn.']

with open("fayl.txt", "r") as file:
    matn = file.read()
print(matn)
Bu yangi qo‘shilgan matn.

  with open("fayl.txt", "r") as file:
    massiv = [satr.strip() for satr in file]
print(massiv)
['', 'Bu yangi qo‘shilgan matn.']

with open("fayl.txt", "r") as file:
    matn = file.read().replace(",", " ").replace(".", " ")
    sozlar = matn.split()
    max_len = max(len(soz) for soz in sozlar)
    uzun_sozlar = [s for s in sozlar if len(s) == max_len]
print("Eng uzun sozlar:", uzun_sozlar)
Eng uzun sozlar: ['qo‘shilgan']

with open("fayl.txt", "r") as file:
    qatorlar_soni = sum(1 for _ in file)
print("Qatorlar soni:", qatorlar_soni)
Qatorlar soni: 2

from collections import Counter
with open("fayl.txt", "r") as file:
    sozlar = file.read().lower().replace(",", " ").replace(".", " ").split()
    chastota = Counter(sozlar)
print(chastota)
Counter({'bu': 1, 'yangi': 1, 'qo‘shilgan': 1, 'matn': 1})

import os
hajm = os.path.getsize("fayl.txt")
print(f"Fayl hajmi: {hajm} bayt")
Fayl hajmi: 27 bayt

malumotlar = ["salom", "dunyo", "python"]

with open("fayl.txt", "w") as file:
    for satr in malumotlar:
        file.write(satr + "\n")

with open("fayl.txt", "r") as original, open("yangi_fayl.txt", "w") as nusxa:
    nusxa.write(original.read())

with open("fayl1.txt") as f1, open("fayl2.txt") as f2, open("birlashtirilgan.txt", "w") as chiqish:
    for satr1, satr2 in zip(f1, f2):
        chiqish.write(satr1.strip() + " " + satr2)

import random
with open("fayl.txt", "r") as file:
    qatorlar = file.readlines()
    print("Tasodifiy qator:", random.choice(qatorlar).strip())
Tasodifiy qator: dunyo

file = open("fayl.txt", "r")
print("Fayl yopildimi?", file.closed)
file.close()
print("Fayl yopildimi?", file.closed)
Fayl yopildimi? False
Fayl yopildimi? True

with open("fayl.txt", "r") as file:
    tozalangan = [satr.strip() for satr in file]
print(tozalangan)
['salom', 'dunyo', 'python']

def sozlar_soni(fayl_nomi):
    with open(fayl_nomi, "r") as file:
        matn = file.read()
        matn = matn.replace(",", " ").replace("\n", " ")
        return len(matn.split())
print(sozlar_soni("fayl.txt"))
3
import string
with open("fayl.txt", "r") as file:
    matn = file.read()
    belgilar = [belgi for belgi in matn if belgi in string.punctuation]
print(belgilar)
[]

for harf in range(65, 91):
    fayl_nomi = f"{chr(harf)}.txt"
    with open(fayl_nomi, "w") as f:
        f.write(f"{chr(harf)} harfi uchun fayl.")

  from string import ascii_lowercase
harflar = list(ascii_lowercase)
miqdor = 5
with open("alifbo.txt", "w") as file:
    for i in range(0, len(harflar), miqdor):
        file.write(" ".join(harflar[i:i+miqdor]) + "\n")
      
