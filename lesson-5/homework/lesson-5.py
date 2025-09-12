1)def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo'lishi kerak.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2020))  # True, 2020 kabisa yili (4 ga bo'linadi va 100 ga bo'linmaydi)
print(is_leap(1900))  # False, 1900 100 ga bo'linadi, lekin 400 ga bo'linmaydi
print(is_leap(2000))  # True, 2000 kabisa yili (400 ga bo'linadi)
print(is_leap(2023))  # False, 2023 kabisa yili emas
True
False
True
False
2)n = int(input("Butun son kiriting: "))
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
      3
Weird
3) def even_numbers_with_if(a, b):
    if a > b:
        return []
    if a % 2 != 0:
        a += 1 
    if a > b:
        return []
    return [a] + even_numbers_with_if(a + 2, b)
a, b = 3, 10
print(even_numbers_with_if(a, b))
[4, 6, 8, 10]

def even_numbers_no_if(a, b):
    start = a + a % 2
    return list(range(start, b + 1, 2))

a, b = 3, 10
print(even_numbers_no_if(a, b))
[4, 6, 8, 10]
