from math import comb


x = int(input())
n = int(input())
s = 0


for i in range(n):
    s += comb(n, i)
