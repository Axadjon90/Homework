1.
lugat = {'olma': 50, 'banan': 20, 'nok': 30, 'anor': 40}
osish_tartibi = dict(sorted(lugat.items(), key=lambda item: item[1]))
pasayish_tartibi = dict(sorted(lugat.items(), key=lambda item: item[1], reverse=True))
print("Qiymatlar bo'yicha o'sish tartibi:", osish_tartibi)
print("Qiymatlar bo'yicha pasayish tartibi:", pasayish_tartibi)
Qiymatlar bo'yicha o'sish tartibi: {'banan': 20, 'nok': 30, 'anor': 40, 'olma': 50}
Qiymatlar bo'yicha pasayish tartibi: {'olma': 50, 'anor': 40, 'nok': 30, 'banan': 20}
2.
lugat = {0: 10, 1: 20}
kalit = 2
qiymat = 30
lugat[kalit] = qiymat
print(lugat)
{0: 10, 1: 20, 2: 30}
3.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
yangi_dic = dic1.copy()
yangi_dic.update(dic2)
yangi_dic.update(dic3)
print(yangi_dic)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
4.
n = 5
lugat = {x: x*x for x in range(1, n+1)}
print(lugat)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
5.
lugat = {x: x**2 for x in range(1, 16)}
print(lugat)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
