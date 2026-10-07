import random

zahlen = list(range(1, 46))  


def ziehen():
    for i in range(6):
        index = random.randrange(0, len(zahlen) - i)  
        gezogen = zahlen.pop(index)
        zahlen.append(gezogen)
    return zahlen[-6:]  


def statistik(anzahl):
    stat = {}
    for i in range(1, 46):
        stat[i] = 0

    for i in range(anzahl):
        for zahl in ziehen():
            stat[zahl] += 1

    for zahl, wert in stat.items():
        print(zahl, ":", wert)


statistik(1000)