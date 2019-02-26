"""
Case-study #9 Автозаправочная станция
Разработчики: Shmatov D. 70%, Bayanova A. 80%
"""

from random import choice
from math import ceil
q = []
def vremya(x):
    t = choice([9,10,11])
    if x%10:
        vr = ceil(x / t)
    elif not x%10:
        x = ceil(x/10) * 10
        vr = ceil(x/t)
    return vr

def och(x):
    count1 = 0
    count2 = 0
    count3 = 0
    if x == "АИ-80":
        if count1 < 3:
            num = 1
            count1 += 1
        return num, count1
    elif x == "АИ-95":
        if count1 < 5:
            num = 3
            count3 += 1
        return num, count3
    elif x == "АИ-98":
        if count1 < 5:
            num = 3
            count3 += 1
        return num, count3
    elif x == "АИ-92":
        if count1 < 5:
            if count2 > count3:
                num = 3
                count3 += 1
                return num, count3
            elif count3 > count2:
                num = 2
                count2 += 1
                return num, count2
            elif count2 == count3:
                num = choice([2,3])
                if num == 2:
                    count2 +=1
                    return num, count2
                else:
                    count3 +=1
                    return num, count3



with open('input.txt') as n:
    with open('azs.txt') as azs:
        for line in azs:
            k = line.split()
            q.append(k)

        for line in n:
            a, b, c = map(str, line.split())
            num, count = och(c)
            count1 = 0
            count2 = 0
            count3 = 0
            if c == "АИ-80":
                count1 += count
            elif c == "АИ-95" or c == "АИ-98":
                count3 += count
            print("В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}".format(a,a,b,c,vremya(int(b)),num))







