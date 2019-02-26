"""
Case-study #9 Автозаправочная станция
Разработчики: Shmatov D. 90%, Bayanova A. 60%
"""

from random import *
from math import ceil
count1 = 0
count2 = 0
count3 = 0

qwer = {}

def vremya(x):
    t = choice([9, 10, 11])
    if int(x)%10:
        vr = ceil(int(x) / t)
    elif not int(x)%10:
        x = ceil(int(x) / 10) * 10
        vr = ceil(int(x) / t)
    return vr

def time(y, x):
    # y - время, к которому нужно прибавить (формата 00:00)
    # x - минуты которые нужно прибвить
    z = int(y[3:]) + int(x)
    h = int(y[:2])
    while z > 59:
        h += 1
        z -= 60
    if z < 10:
        z = "0" + str(z)
    if h < 10:
        hour = "0" + str(h)
        return hour + ":" + str(z)
    return str(h) + ':' + str(z)

def status(z1, z2, z3):
    #x - макс кол-во в очереди
    #y - виды марок
    #z - очередь
    q = []
    with open('azs.txt') as azs:
        for l in azs:
            k = l.split()
            q.append(k)
        m = q[2][2] + " " + q[2][3] + " " + q[2][4]

    print("Автомат №{}  максимальная очередь:{}. Марки бензина: {} -> {}".format(q[0][0],q[0][1],q[0][2],z1 * "*"))
    print("Автомат №{}  максимальная очередь:{}. Марки бензина: {} -> {}".format(q[1][0],q[1][1],q[1][2],z2 * "*"))
    print("Автомат №{}  максимальная очередь:{}. Марки бензина: {} -> {}".format(q[2][0],q[2][1],m, z3 * "*"))


with open('input.txt') as n:
    with open('azs.txt') as azs:


        for line in n:
            a, b, c = map(str, line.split())
            t = time(str(a),vremya(b))



            if c == "АИ-80":
                if count1 < 3:
                    count1 += 1
                    num = 1
                    qwer.update({a: "В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                         vremya(int(b)),
                                                                                                  num)})
                    qwer.update({t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(t, a, b, c,vremya(int(b)), num)})

                else:
                    qwer.update({a:
                        "В {} новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.".format(a, a, b, c,
                                                                                                            vremya(
                                                                                                                int(b)))})
            elif c == "АИ-95":
                if count3 < 5:
                    count3 += 1
                    num = 3
                    qwer.update({a:"В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                  vremya(int(b)),
                                                                                                  num)})
                    qwer.update({
                                    t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                        t, a, b, c, vremya(int(b)), num)})
                else:
                    qwer.update({a:
                        "В {} новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.".format(a, a, b, c,
                                                                                                            vremya(
                                                                                                                int(b)))})
            elif c == "АИ-98":
                if count3 < 5:
                    count3 += 1
                    num = 3
                    qwer.update({a:"В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                  vremya(int(b)),
                                                                                                  num)})
                    qwer.update({
                                    t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                        t, a, b, c, vremya(int(b)), num)})
                else:
                    qwer.update({a:
                        "В {} новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.".format(a, a, b, c,
                                                                                                            vremya(
                                                                                                                int(b)))})
            elif c == "АИ-92":
                if count2 > count3:
                    if count3 < 5:
                        count3 += 1
                        num = 3
                        qwer.update({a: "В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                      vremya(int(b)),
                                                                                                      num)})
                        qwer.update({
                                        t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                            t, a, b, c, vremya(int(b)), num)})
                elif count3 > count2:
                    if count2 < 4:
                        count2 += 1
                        num = 2
                        qwer.update({a:"В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                      vremya(int(b)),
                                                                                                      num)})
                        qwer.update({
                                        t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                            t, a, b, c, vremya(int(b)), num)})
                elif count2 == count3:
                    qw = randint(2, 3)
                    if qw == 2:
                        if count2 < 4:
                            count2 += 1
                            num = 2
                            qwer.update({a: "В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                          vremya(int(b)),
                                                                                                          num)})
                            qwer.update({
                                            t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                                t, a, b, c, vremya(int(b)), num)})
                    elif qw == 3:
                        if count3 < 5:
                            count3 += 1
                            num = 3
                            qwer.update({a:"В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}.".format(a, a, b, c,
                                                                                                          vremya(int(b)),
                                                                                                          num)})
                            qwer.update({
                                            t: "В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул автомат № {}".format(
                                                t, a, b, c, vremya(int(b)), num)})


            for i in range(0, 24):
                if i < 10:
                    ht = "0" + str(i)
                else:
                    ht = str(i)
                for j in range(0, 60):
                    if j < 10:
                        mt = "0" + str(j)
                    else:
                        mt = str(j)
                    tt = ht + ":" + mt
                    if tt in qwer:
                        if qwer.get(tt)[-1] == "1":
                            count1 -= 1
                        elif qwer.get(tt)[-1] == "2":
                            count2 -= 1
                        elif qwer.get(tt)[-1] == "3":
                            count3 -= 1

                        print(qwer.pop(tt))
                        status(count1, count2, count3)




