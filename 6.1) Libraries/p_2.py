from random import shuffle


n = int(input("Введите количество элементов списка \n"))
spis = []
prov = []


for i in range(1, n + 1):
    spis.append(str(i))


for j in range(n * 10000):
    shuffle(spis)
    a = ""
    for num, el in enumerate(spis):
        a += el
    if prov.count(a) < 1:
        prov.append(a)


print(prov)
print(len(prov))
