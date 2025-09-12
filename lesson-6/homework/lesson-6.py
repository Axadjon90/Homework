1)def insert_underscore(txt):
    unli = "aeiouAEIOU"
    result = []
    i = 0
    length = len(txt)

    while i < length:
        result.append(txt[i])
        
        if (i + 1) % 3 == 0 and i != length - 1:
            if txt[i] in unli or (i + 1 < length and txt[i + 1] == '_'):
                result.append(txt[i + 1])
                if i + 2 < length:
                    result.append('_')
                    i += 1
                else:
                    i += 1
            else:
                result.append('_')
        i += 1

    return "".join(result)

print(insert_underscore("salom"))
print(insert_underscore("assalom"))
print(insert_underscore("abcabcabcdeabcdefabcdefg"))
sal_om
ass_alom
abc_abc_abc_deab_cd_efab_cd_efg

2)n = int(input())
for i in range(n):
    print(i ** 2)
  5
0
1
4
9
16

3)i = 1
while i <= 10:
    print(i)
    i += 1
1
2
3
4
5
6
7
8
9
10

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

n = int(input("Son kiriting: "))
yigindi = 0
for i in range(1, n + 1):
    yigindi += i
print("Yig'indi:", yigindi)
5
Yig'indi: 15

n = int(input("Son kiriting: "))
for i in range(1, 11):
    print(n * i)
6
6
12
18
24
30
36
42
48
54
60

raqamlar = [12, 75, 150, 180, 145, 525, 50]

for son in raqamlar:
    if son > 500:
        break
    if son % 5 == 0 and son <= 150:
        print(son)
75
150
145

son = int(input("Son kiriting: "))
raqam_soni = len(str(abs(son)))
print("Chiqish:", raqam_soni)
1
Chiqish: 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

royxat1 = [10, 20, 30, 40, 50]

for i in reversed(royxat1):
    print(i)
50
40
30
20
10

for i in range(-10, 0):
    print(i)
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

for i in range(5):
    print(i)
else:
    print("Bajarildi!")
0
1
2
3
4
Bajarildi!

print("25 dan 50 gacha tub sonlar:")

for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
25 dan 50 gacha tub sonlar:
29
31
37
41
43
47

print("Fibonachchi ketma-ketligi:")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
Fibonachchi ketma-ketligi:
0 1 1 2 3 5 8 13 21 34 

n = int(input("Son kiriting: "))
faktorial = 1
for i in range(1, n + 1):
    faktorial *= i
print(f"{n}! = {faktorial}")
9! = 362880

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    result = []

    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
        else:
            diff = c1[elem] - c2[elem]
            if diff > 0:
                result.extend([elem] * diff)

    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
        else:
            diff = c2[elem] - c1[elem]
            if diff > 0:
                result.extend([elem] * diff)

    return result
  print(uncommon_elements([1, 1, 2], [2, 3, 4]))
[1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 
[1, 2, 3, 4, 5, 6]
[1, 2, 2, 5]
