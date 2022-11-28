alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
slov = {" ": " "}

for num, bk in enumerate(alp, start=1):
    slov[bk] = str(num)

a = input()
b = ""

for num, bk in enumerate(a, start=1):
    b += slov[bk] + "."

b = b[0:-1]
print(b)