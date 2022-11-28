import string


def prep(x):
    for p in string.punctuation:
        if p in x:
            x = x.replace(p, "")
    return x


a = prep(input())

b = a.split(" ")

c = ""


for i in range(len(b)):
    if c.find(b[i]) < 0:
        c += b[i] + " "

d = c.split(" ")

for i in range(len(d) - 1):
    print(d[i], " - ", b.count(d[i]))
