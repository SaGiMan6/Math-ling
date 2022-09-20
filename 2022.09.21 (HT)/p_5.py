import json


with open("Pokemon.json", mode="r") as pok:
    a = json.load(pok)


h_height = float(input("Введите рост \n"))
h_weight = float(input("Введите вес \n"))


for num, el in enumerate(a):
    if el["weight"] != "(None kg)" or el["height"] != "(Nonem)":
        p_height = float(str(el["height"])[str(el["height"]).find("(") + 1:str(el["height"]).find(")") - 1])
        p_weight = float(str(el["weight"])[str(el["weight"]).find("(") + 1:str(el["weight"]).find(")") - 3])
        if p_height <= h_height and p_weight <= h_weight:
            print(el["name"])
