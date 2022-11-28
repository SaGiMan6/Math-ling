def sln(x):
    for i in range(len(x)):
        x[i] = x[i] + " \n"
    return x


a = ["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", "Ноль"]
c = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Zero"]

with open("p_1_1.txt", mode="w") as my_file:
    my_file.writelines(sln(a))

with open("p_1_1.txt", mode="r") as myy_file:
    b = myy_file.readlines()
    for i in range(len(b)):
        b[i] = c[i]
    with open("p_1_2.txt", mode="w") as ym_file:
        ym_file.writelines(sln(b))
