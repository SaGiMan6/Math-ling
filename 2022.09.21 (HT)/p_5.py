import json


with open("Pokemon.json", mode="r") as pok:
    a = json.load(pok)


x = int(input())
y = int(input())


for num, el in enumerate(a):
    m = el['height']
