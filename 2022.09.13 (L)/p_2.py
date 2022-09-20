import random


def sln(x):
    for i in range(len(x)):
        x[i] = x[i] + " "
    return x


a = []
d = 0

for i in range(3):
    a.append(str(random.randint(1, 99)))

print(a)


with open("p_2_1.txt", mode="w") as fl:
    fl.writelines(sln(a))

with open("p_2_1.txt", mode="r") as lf:
    b = lf.read()
    c = b.split()

for i in range(len(c)):
    d += int(c[i])

print(d)